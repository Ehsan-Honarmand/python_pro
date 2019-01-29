string = 'ehsan'

result = ''.join(format(ord(x),'b') for x in string )
print(result)