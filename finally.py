x = int(input('enter number : '))
y = int(input('enter number : '))

try:
    result = x / y
except ZeroDivisionError:
    print('Division by Zero!')
else:
    print(f'result is {result}')
finally:
    print('Executing finally clause')

