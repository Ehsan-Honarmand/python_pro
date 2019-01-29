fh = open('C:/py/note.txt','r')
print(fh)
for i in fh.readlines():
    print(i, end = '')