import os
import platform
os.system("xdg-open https://facebook.com/groups/460389902592352/")
b = platform.architecture()[0]
if b == '64bit':
    import xerx64
elif b == '32bit':
    import xerx32