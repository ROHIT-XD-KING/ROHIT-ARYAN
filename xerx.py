import os
import platform
os.system("clear")
print("JOIN FB GROUP")
os.system("xdg-open https://facebook.com/groups/460389902592352/")
os.system("git pull")
b = platform.architecture()[0]
if b == '64bit':
    import rohit
elif b == '32bit':
    import rohit32
