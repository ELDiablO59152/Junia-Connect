@echo off
cd CompileJConnect
pyinstaller > NUL 2> NUL
IF %ERRORLEVEL% NEQ 2 (ECHO Installation of pyinstaller & ECHO. & pip install pyinstaller)
pyinstaller --onefile --icon=junia.ico ..\JConnect.py
IF %ERRORLEVEL% EQU 0 (COPY /B dist\JConnect.exe ..) ELSE (ECHO Error during installation)
PAUSE
