import sys
loop = 0
number1 = int(input('Enter first number: '))
operator = input('Enter operator: ')
number2 = int(input('Enter second number: '))
if operator == '+':
    print(number1 + number2)
elif operator == '-':
    print(number1 - number2)
elif operator == '*':
    print(number1 * number2)
elif operator == '/':
    print(int(number1 / number2),'remainder',number1 % number2)
else:
    print('Invalid input')

while loop == 0:
    runagain = input('Run again(Y/N?): ')
    if runagain == 'Y':
        break
    elif runagain == 'N':
        print('Calculator terminated')
        sys.exit()
    else:
        print('Invalid input')
            
