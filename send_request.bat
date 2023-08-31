REM Wait for 10 seconds
timeout /t 10 >nul

@echo off

REM Activate virtual environment
call %WECHAT_BOT_PROJECT_PATH%\venv\Scripts\activate.bat

REM Run Python script
python %WECHAT_BOT_PROJECT_PATH%\send_request.py

pause >nul
