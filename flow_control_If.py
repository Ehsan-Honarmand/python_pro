import sys 
if sys.version_info.major < 3:
    print('version 2.x')
elif sys.version_info.major > 3:
    print('Future')
else:
    print('version 3.x')