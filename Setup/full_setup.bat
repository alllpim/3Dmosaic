Powershell -Command "Invoke-WebRequest 'https://netix.dl.sourceforge.net/project/portable-python/Portable Python 3.10/Portable Python-3.10.0 x64.exe' -O Python_3.10_Archive.exe"

Python_3.10_Archive.exe -y

move "Portable Python-3.10.0 x64/App/Python" "../Python"

del "Python_3.10_Archive.exe"

rmdir /Q /S "Portable Python-3.10.0 x64"

..\Python\python.exe -m pip install --upgrade pip --no-warn-script-location

..\Python\python.exe -m pip install -r .\requirements.txt --no-warn-script-location
