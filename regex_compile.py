#regex example in python 
import re
age = re.compile('\d+')
se = age.search('I am 27 years old')

print(se.group())
