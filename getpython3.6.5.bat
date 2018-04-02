@echo off
title getpython3.6.5.bat
cls
bitsadmin  /transfer getpython /download  /priority normal https://www.python.org/ftp/python/3.6.5/python-3.6.5.exe  C:\Users\%username%\Documents\PythonAutoTyper\python3.6.5.exe
timeout 5
exit