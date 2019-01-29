l = [1,2,3,8,6,9,7,'a','c','b']

for i in range(0,len(l)):
    print(i,l[i])

del l[-3:]
l.sort()
print(l)

l[0]=0
print(l)

l.remove(0)
print(l)

l.extend([10,11,12])
print(l)

l.append(13)
print(l)
l.pop()
print(l)

