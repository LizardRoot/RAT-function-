import os 
import shutil
import getpass

path = os.path.abspath(__file__)
print(path)

dir = os.path.abspath(os.curdir) + '\\1.txt'
print(dir)

autorun = os.getenv("SystemDrive") + '\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup'
print(autorun)

shutil.copyfile(path, autorun + '\\test.txt')