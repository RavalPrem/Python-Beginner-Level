#exponents (**) used for counting the power of given value
val1 = 2
print('\nvalue : ',val1)
print('square : ',val1 ** 2)
print('Cube : ',val1 ** 3)
print('\n')

#floor division (used for removing the fractoinal part of number)
val2 = 2
print('\nThe value : ', val2)
print('The floor division : ', val2 // 3)
print('\n')

#identity operator
a = 5
b = 5
print('a = 5 and b = 5 so a is b :',a is b)
print('a = 5 and b = 5 so a is not b :', a is not b)

print('\nThe id keyword using')
'''
explanation --> address will be same if two or more variables have same values
means if tow or more variable had same values , the id will be same means the address will be same for both
'''
valA = 10
valB = 10
print('\nid keyword used down below')
print('id of valA :',id(valA))
print('id of valB :',id(valB))

#membership operaotr
print('\nChecking that the number is in the list using "in" keyword')
ls1 = [10, 20, 30, 40, 50]
print('\nThe list down below\n',ls1)
print('\n20 is in list',20 in ls1)

#I know ternary is old
print('\nused Ternary operator\n')
num1 = 15
num2 = 20
maximum = num1 if num1 > num2 else num2
print('num1 :',num1)
print('num2 :',num2)
print('\nMaximum num :',maximum)

print('\n')