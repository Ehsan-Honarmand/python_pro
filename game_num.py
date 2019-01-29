import random 
javab = random.randint(1,99)

name = input('hi , what is your name ?')
hads = input('what is your guess for num ?')
hads = int(hads)

while hads != javab :
    if hads > javab :
        print('%s ,mine is smaller of number %d  ' % (name,hads))
    else:
        print('%s ,mine is larger of number %d  ' % (name,hads))
    
    hads = input(' what is your guess for num ? ')
    hads = int(hads)

name = name.upper()
print('woooow , %s you did it , YOU ROCK!!!!' % name )
