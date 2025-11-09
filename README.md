<h1>Scripts</h1>

*Scripts are relational and can only be run in the scripts directory after they have run they put you back in the top directory*

<h3>setup_linux.sh</h3>
This is a bash script that sets up everything this program needs to run you should exicute it when you clone the directory from git


<h3>clean.sh</h3>
This is is a function that gives you a view of what the git hub repo will look like. This isn't nessicary to run because all the irrelivant files will be ignored by the .gitignore however I like how clean it makes the code lool.

>------------

``` bash
# Replace my_script 
cd scripts
chmod +x my_script.sh
. my_script.sh
```

>------------

<h1>How to run severs</h1>
Create two bash terminals

In the first

``` bash
cd flask_backend
source .venv/bin/activate
flask --app app.py run --debug
```

In the second

``` bash
# tigerhacks2025

This repository contains a small web project with a Flask backend and a React frontend. The `scripts/` folder contains convenience scripts to set up the development environment on Linux and Windows.

This README covers project layout, how to set up the project on Linux and Windows, how to run the backend and frontend, and a short troubleshooting section.

## Repository layout

- `flask_backend/` - Flask backend code and `requirements.txt`.
	- `app.py`, `core.py`, `db.py`, `nodal_logistics.py`, `node_logictest.py`
- `react_frontend/` - React/Vite frontend source in `src/` and `package.json`.
- `scripts/` - helper scripts:
	- `setup_linux.sh` - sets up the Linux development environment (node, python venv, pip deps, npm deps)
	- `setup_windows.ps1` - PowerShell script to help set up on Windows (uses winget if available)
	- `clean.sh` - a helper to tidy the workspace (optional)
- `README.md` - this file

## Requirements

- Node.js (recommend current LTS; project was tested with Node 18+)
- npm (bundled with Node)
- Python 3.8+ (3.10+ recommended)
- pip
- On Windows: `winget` is optional but the provided `setup_windows.ps1` will use it to install Node/Python when available. Run PowerShell as Administrator if you want the script to install packages.

## Quick setup (Linux)

The repository includes `scripts/setup_linux.sh` which automates most steps for Linux (and WSL). From the repository root:

```bash
cd scripts
./setup_linux.sh
```

What that script does (high level):
- Updates apt packages
- Installs Node, npm, Python, pip, and venv tools
- Creates a Python virtual environment at `flask_backend/.venv` and installs Python dependencies from `flask_backend/requirements.txt`
- Runs `npm install` in `react_frontend/`

If you prefer to run the steps manually:

```bash
# Backend
cd flask_backend
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

# Frontend (in a second terminal)
cd ../react_frontend
npm install
npm run dev
```

To run the backend (after creating and activating the venv):

```bash
cd flask_backend
source .venv/bin/activate
flask --app app.py run --debug
```

## Quick setup (Windows)

Use the PowerShell helper `scripts/setup_windows.ps1`. Run PowerShell (preferably as Administrator if you want automatic installs via winget) and from the repository root:

```powershell
cd C:\path\to\repo\scripts
.\setup_windows.ps1
```

What the script does:
- Detects whether `node` and `python` are installed; if missing and `winget` is available it will attempt to install them.
- Creates a Python venv at `flask_backend\.venv` and installs Python dependencies using the venv's pip (no activation required inside scripts).
- Runs `npm install` inside `react_frontend`.

Manual Windows commands (if you prefer):

```powershell
# Backend
cd .\flask_backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1   # or use Activate.bat in cmd
python -m pip install --upgrade pip
pip install -r requirements.txt

# Frontend (separate terminal)
cd ..\react_frontend
npm install
npm run dev
```

Notes:
- If PowerShell policy prevents running scripts (Activation scripts), you can call the venv pip directly: `.
.venv\Scripts\pip.exe install -r requirements.txt`.
- The provided `setup_windows.ps1` uses the venv pip directly to avoid activation policy issues.

## How to run the app

1. Start the backend:

	 - Activate venv and run Flask (see the commands above). By default Flask will run on `http://127.0.0.1:5000`.

2. Start the frontend:

	 - From `react_frontend/`, run `npm run dev`. Vite will start a dev server, typically on `http://localhost:5173` (check CLI output).

3. Open the frontend URL in your browser. The frontend communicates with the backend (CORS or proxy may need configuration depending on how APIs are exposed).

## Troubleshooting

- If `setup_windows.ps1` reports that winget is not available: install `winget` (from Microsoft) or install Node and Python manually.
- If venv creation fails: ensure you have the `python3-venv` package (Linux) or that your Python installation includes venv (Windows installer option).
- If `pip install -r requirements.txt` fails: inspect the error and try upgrading pip first:

	```bash
	python -m pip install --upgrade pip
	python -m pip install -r requirements.txt
	```

- If `npm install` errors: remove `node_modules/` and try `npm cache clean --force` then `npm install` again.

- Check `scripts/bad_output.txt` for logged errors when using the setup scripts.

## Development notes

- The Flask backend entry point is `flask_backend/app.py`.
- The React app root is `react_frontend/src/` with `main.jsx` and `App.jsx`.

## Next steps and contributions

- Add tests for backend endpoints and frontend components.
- Add an environment configuration (example `.env`) and document API URLs for local development.
- Improve CI to run linting and tests.

If you want, I can add a small `scripts/README.md` with Windows troubleshooting steps or expand this file with example API usage.
