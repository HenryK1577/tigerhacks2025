<#
    setup_windows.ps1
    Windows setup script for the project.

    What it does:
    - Checks for node and python and attempts a winget install if missing (if winget exists).
    - Creates a Python venv in `flask_backend` and installs requirements using the venv's pip.
    - Runs `npm install` in `react_frontend`.

    Notes:
    - Run PowerShell as Administrator if you want winget to be able to install packages.
    - If winget is not available this script will log the missing pieces and continue.
#>

$logFile = Join-Path -Path (Split-Path -Parent $MyInvocation.MyCommand.Definition) -ChildPath "bad_output.txt"

# Clear previous log
if (Test-Path $logFile) { Remove-Item $logFile -ErrorAction SilentlyContinue }

function Log-Error($message) {
    Write-Host "ERROR: $message" -ForegroundColor Red
    Add-Content -Path $logFile -Value $message
}

Write-Host "This is a setup script for Windows systems."

$answer = Read-Host "Are you sure you want to continue? (Y/n)"
if ($answer -and $answer.ToLower().StartsWith('n')) {
    Write-Host "Exiting setup."; exit 1
}

# Helper: get script root and project directories
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Definition
$backendDir = Resolve-Path -Path (Join-Path $scriptDir '..\flask_backend') -ErrorAction SilentlyContinue
$frontendDir = Resolve-Path -Path (Join-Path $scriptDir '..\react_frontend') -ErrorAction SilentlyContinue

# Check for winget
$hasWinget = $false
if (Get-Command winget -ErrorAction SilentlyContinue) { $hasWinget = $true }

# ------------------------
# Node.js check & install
# ------------------------
try {
    if (-not (Get-Command node -ErrorAction SilentlyContinue)) {
        if ($hasWinget) {
            Write-Host "Node.js not found. Attempting to install via winget..."
            winget install --id OpenJS.NodeJS -e -h || throw "Failed to install Node.js via winget"
        } else {
            Log-Error "Node.js not found and winget is not available. Please install Node.js manually from https://nodejs.org/"
        }
    } else {
        Write-Host "Node.js is installed."
    }
} catch {
    Log-Error "Node.js installation failed: $($_.Exception.Message)"
}

# ------------------------
# Python check & install
# ------------------------
try {
    if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
        if ($hasWinget) {
            Write-Host "Python not found. Attempting to install via winget..."
            winget install --id Python.Python.3 -e -h || throw "Failed to install Python via winget"
        } else {
            Log-Error "Python not found and winget is not available. Please install Python 3+ from https://www.python.org/"
        }
    } else {
        Write-Host "Python is installed."
    }
} catch {
    Log-Error "Python installation failed: $($_.Exception.Message)"
}

# ------------------------
# Setup backend
# ------------------------
if ($backendDir) {
    try {
        Set-Location -Path $backendDir

        Write-Host "Creating Python virtual environment in $backendDir..."
        & python -m venv .venv || throw "Failed to create virtual environment"

        $venvPip = Join-Path -Path (Join-Path $backendDir '.venv') -ChildPath 'Scripts\pip.exe'
        if (-not (Test-Path $venvPip)) { throw "pip not found in venv at $venvPip" }

        Write-Host "Upgrading pip and installing backend requirements..."
        & $venvPip install --upgrade pip || throw "Failed to upgrade pip"
        & $venvPip install -r requirements.txt || throw "Failed to install backend requirements"

        Write-Host "Backend setup complete."
    } catch {
        Log-Error "Backend setup failed: $($_.Exception.Message)"
    }
} else {
    Log-Error "Backend directory not found relative to script location: $scriptDir"
}

# ------------------------
# Setup frontend
# ------------------------
if ($frontendDir) {
    try {
        Set-Location -Path $frontendDir
        Write-Host "Installing frontend dependencies in $frontendDir..."
        npm install || throw "Failed to install frontend dependencies"
        Write-Host "Frontend setup complete."
    } catch {
        Log-Error "Frontend setup failed: $($_.Exception.Message)"
    }
} else {
    Log-Error "Frontend directory not found relative to script location: $scriptDir"
}

# ------------------------
# Finish
# ------------------------
Set-Location -Path $scriptDir
Clear-Host
Write-Host "---------------"
Write-Host "Setup complete!"
Write-Host "---------------"

if (Test-Path $logFile) {
    Write-Host "`nSome steps failed. Check $logFile for details." -ForegroundColor Yellow
}
