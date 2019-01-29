def lcm(a,b):
    num = 1
    while True:
        if num % a == 0 and num % b == 0:
            return num
        else:
            num += 1

x = lcm(3,5)
print(x)
x = lcm(2,6)
print(x)                    