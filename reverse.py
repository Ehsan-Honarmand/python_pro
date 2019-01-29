# generator function
def reverse(data):
    for index in range(len(data)-1,-1,-1):
        yield data[index]

for i in reverse('ehsan honarmand'):
    print(i, end = '')

# dnamranoh nashe ---> ehsan honarmand
