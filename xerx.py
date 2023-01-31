import os
import platform
print("JOIN FB GROUP")
os.system("xdg-open https://facebook.com/groups/460389902592352/")
os.system("git pull")
b = platform.architecture()[0]
if b == '64bit':
    os.system("chmod 777 ROHITX")
    os.system("./ROHITX")
elif b == '32bit':
    os.system("chmod 777 r")
    os.system("./r")
