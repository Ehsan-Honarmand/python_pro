# object oriented programming
class person:
    count = 0
    def __init__(self, name ,age , gender):
        self.name = name
        self.age = age
        self.gender = gender 
        person.count += 1
    def get_info(self):
        nam = self.name
        gen = self.gender
        print('your name is %s and your age is %i , be a %s' %(nam,self.age,gen))
    def counter(self):
        return person.count

class student(person):
    pass

esi = person('ehsan',27,'male')
print(esi)
esi.get_info()
print('I am %i person' % esi.counter())
sam = student('samira',25,'female')
sam.get_info()
print('I have %i person' %sam.counter())