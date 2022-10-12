# Junia-Connect
Short script to authenticate against Junia firewall. Can be launched on Windows startup. It will check the correct WiFi name before authentication.

Make sure you have installed requests :
```
pip install requests
```

You can launch the script for the prompt method or by giving the credentials as arguments with the commands :
```
python JConnect.py
python JConnect.py mail=[mail address] password=[password] debug
```
A simpler script is provided with your hardcoded credentials :
```
python JConnectNoPrompt.py
```

You can also compile it with pyinstaller (pip install pyinstaller) by executing the CompileJConnect.bat script to get an executable.

Like so, you can put it in your `C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp` folder to launch it at every startup but only run when you are connected to `JUNIA_STUDENTS`.

By creating a shortcut, you can also give your credentials in the shortcut as you can do with the python one in the target :
```
"C:\...\JConnect.exe" mail=[mail address] password=[password] debug
```
