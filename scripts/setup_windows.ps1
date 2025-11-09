# setup.ps1
# Windows setup script with error logging

$logFile = "bad_output.txt"

# Clear previous log
if (Test-Path $logFile) { Remove-Item $logFile }

function Log-Error($message) {
    Write-Host "ERROR: $message" -ForegroundColor Red
    Add-Content -Path $logFile -Value $message
}

Write-Host "This is a setup script for Windows systems."

$answer = Read-Host "Are you sure you want to continue? (Y/n)"
if ($answer -ne "y" -and $answer -ne "") {
    Write-Host "Exiting setup."
    exit 1
}

# ------------------------
# Node.js check & install
# ------------------------
try {
    if (-not (Get-Command node -ErrorAction SilentlyContinue)) {
        Write-Host "Node.js not found. Attempting to install via winget..."
        winget install --id OpenJS.NodeJS -e || throw "Failed to install Node.js"
    } else {
        Write-Host "Node.js is installed."
    }
} catch {
    Log-Error "Node.js installation failed: $_"
}

# ------------------------
# Python check & install
# ------------------------
try {
    if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
        Write-Host "Python not found. Attempting to install via winget..."
        winget install --id Python.Python.3 -e || throw "Failed to install Python"
    } else {
        Write-Host "Python is installed."
    }
} catch {
    Log-Error "Python installation failed: $_"
}

# ------------------------
# Setup backend
# ------------------------
try {
    Set-Location ..\flask_backend
    python -m venv .venv || throw "Failed to create virtual environment"
    & .\.venv\Scripts\Activate.ps1
    pip install --upgrade pip || throw "Failed to upgrade pip"
    pip install -r requirements.txt || throw "Failed to install backend requirements"
    deactivate
    Write-Host "Backend setup complete."
} catch {
    Log-Error "Backend setup failed: $_"
}

# ------------------------
# Setup frontend
# ------------------------
try {
    Set-Location ..\react_frontend
    npm install || throw "Failed to install frontend dependencies"
    Write-Host "Frontend setup complete."
} catch {
    Log-Error "Frontend setup failed: $_"
}

# ------------------------
# Finish
# ------------------------
Set-Location ..\
Clear-Host
Write-Host "---------------"
Write-Host "Setup complete!"
Write-Host "---------------"

if (Test-Path $logFile) {
    Write-Host "`nSome steps failed. Check $logFile for details." -ForegroundColor Yellow
}
