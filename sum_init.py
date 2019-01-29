total = 0
count = 0

while True:
    num = input('enter number : ')
    if num == 'done':
        print(f'sum of all entered numbers is {total}')
        print(f'count of total numbers is {count}')
        break
    else:    
        try:
            total += float(num)
        except:
            print('invalid number')
            continue
        count += 1 

