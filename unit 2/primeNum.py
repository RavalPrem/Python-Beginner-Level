num = int(input('Enter num : '))
for i in range(2,num):
    if num%i==0:
        print('\n',num,'is not a prime number')
        break
else:
    print('\n',num,'is a prime number')

print('\n\nDo it with the while loop\n')
num2 = int(input('Enter number : '))
a = 2
while a < num2:

    if num2%i==0:
        print('\n',num2, 'is not a prime number')
        break
    a+=1
else:
    print('\n',num2, 'is a prime number')

print()