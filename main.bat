@echo off
where uv >nul 2>nul
IF ERRORLEVEL 1 (
    echo [INFO] uv not found. Installing via pip...
    py -3 -m pip install --upgrade pip
    py -3 -m pip install uv
) ELSE (
    echo [INFO] uv is already installed.
)

IF NOT EXIST ".venv" (
    echo [INFO] Creating virtual environment with uv (Python 3.13)...
    uv venv .venv --python 3.13
)

call .venv\Scripts\activate.bat
echo [INFO] Installing dependencies from requirments.txt...
uv pip install -r requirements.txt

echo [INFO] Running main.py
uv run python main.py
