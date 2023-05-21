from math import *

print('Welcome!')
num1 = input('Enter a number: ')
numerator = input('Enter the numerator (ej, *, +, /): ')
num2 = input('Enter another number: ')

result = float

if numerator == '/':
    result = float(num1) / float(num2)

if numerator == '+':
    result = float(num1) + float(num2)

if numerator == '*':
    result = float(num1) * float(num2)

if numerator == '-':
    result = float(num1) - float(num2)

print('The Result is: ' + result.__str__())

exit = input('Press any key to exit...')

