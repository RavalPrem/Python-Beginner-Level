print('\nPrinting with two parameters')
for i in range(1,11):
    print(i,end=' ')

print('\n\nWith 3 parameters')
for i in range(0,11,2):
    print(i,end=' ')

print('\n\n Print in reverse')
for i in range(20,0,-1):
    print(i ,end=' ')

print('\n\n pattern 1 left to right *')
for i in range(1,6):
    for j in range(1, i+1):
        print('*', end=' ')
    print()

print('\n\n Pattern with only one for loop')
for i in range(1,6):
    print('* '*i)

print('\n\n number pyramid why?')
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=' ')
    print()

print('\n\n number pyramid2 why?')
for i in range(1,6):
    for j in range(1,i+1):
        print(i,end=' ')
    print()

print('\n\n Pyramid with extra variable')
a = 0
for i in range(1,5):
    for j in range(1,i+1):
        print(a,end=' ')
        a+=1
    print()

print('\n')
