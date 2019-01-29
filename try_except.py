while True:
    try:
        num = int(input('enter number! '))
        print(f'YOUR number is {num}')
        break
    except ValueError:
        print('Oops!!! your number is invalid')

