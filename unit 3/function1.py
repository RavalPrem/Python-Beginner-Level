def printHello():
    print('Hello')
printHello()

def add(a,b):
    print(f'addition of {a} + {b} = {a + b}')

add(2,3)

print('\n')

def defaultValue(a,b = 5):
    print(f'addition in default function {a} + {b} = {a + b}')
defaultValue(2,7)
defaultValue(2)

#passing the keyword when calling the method
def func1(a = 2,b = 0):
    print(f'\nsubtraction of {a} - {b} = {a - b}')
func1(b = 5) #you can change the value of b using the keyword b when calling the method

#with return
print('\nFunction with return')
def ret1(a,b):
    c = a / b
    return c
div1 = ret1(21,7)
print('\nThe division of 21 / 7 =',div1)


#variable length argument
print('\nFunction named variable length argument')
def num1(*a):
    print(f'The value of a ->',a)
    print(f'the type of a -> {type(a)}')

num1(10,20,30)

#keyword varible length function
print('\nFunction that takes the variable with the keyword')
def person1(**a):
    print(f'the a variable -> {a}')
    print(f'Type of a variable -> {type(a)}')

person1(name='prem',rollNo=84)

#anonymous function
print('\nanonymous function is one line function used in small operations')
theadd = lambda a,b:a+b
print(f'The addition 2 + 3 = {theadd(2,3)}')

print()