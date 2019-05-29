@echo off

echo Activating venv...
call venv3\Scripts\activate.bat
echo Starting server...
start "PriProBot" python PriProBot\main.py
call venv3\Scripts\deactivate.bat
echo Exiting venv.
