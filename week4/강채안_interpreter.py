arithmeticexpression = input('산술식 입력하세욤: ')

x = float(arithmeticexpression[0])
y = arithmeticexpression[1]
z = float(arithmeticexpression[2])


if y == '+':
    print(x + z)
elif y == '-':
    print(x-z)
elif y == '*':
    print(x*z)
else:
    print(x/z)




