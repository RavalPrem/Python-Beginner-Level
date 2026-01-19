ls1 = [1, 'ExpressJs', 1+5j, 'another string', 3.14567]
ls2 = [2, 4.555, 'string in list', 'c', 4+5j]
ls3 = ls1 + ls2
print(ls3)

#slicing
print('\nSlicing from 0 to 2 \'Because 3 is exclusive value so it doesn\'t included\'')
print(ls1[:3])

#append
ls4 = [100,200,300]
print('\nAppend the 400 in the list addded to last')
ls4.append(400)
print(ls4)

#extends --> used for adding multiple values
ls4.extend([500, 700, 1000, 500]) 
print('\nExtend used to add 500, 700, 1000, 500')
print(ls4)

# ! insert --> insert value using index number
ls5 = [100, 'React JS',1+2j ,'GSAP']
print('\n -Insert used for adding value using index number')
ls5.insert(1,'String at index 1 in list ls5')
print(ls5)

#remove
ls5.remove(100)
print(f'\n removed 100 \n{ls5}')
print('\nAlso this have issue that it removes first occurence')
#example
ls6 = [1,2,2,2,3,5,7]
print(f'\nls6 Before remove : {ls6}')
ls6.remove(2)
print(f'ls6 after remove : {ls6}')


#pop
print('\nPop in list remove last added value or last value of list')
ls5.pop()
print(f'{ls5}')

#clear
print(f'\nThe clear used')
ls5.clear()
print(f'the ls5 : {ls5}')

#copy
lsOriginal = [1,2,3]
lssecondName = lsOriginal
lssecondName.clear()
print(f'\nThe original : {lsOriginal} \nand lssecondName : {lssecondName}')
print('\nSee that this is the issue without copy, the second name is initialize to the list')
print('\nSo for the copy used the copy method')
lsOrg1 = [1,2,3]
lsCopy = lsOrg1.copy()
lsCopy.clear()
print(f'\nlsOrg1 : {lsOrg1} \nlsCopy : {lsCopy}')

#max, min, sum as always 
lsNum = [1,5,7,2,10]
print(
    f'\n lsNum : {lsNum}', 
    '\nmax number : ',max(lsNum),
    '\nMin number : ',min(lsNum)
)
lsString = ['MongoDB','Express Js','React Js','Node JS']
print(
    f'\nlsString : {lsString}',
    '\nMax : ',max(lsString),
    '\nMin : ',min(lsString)
)
print(
    f'\nlsNum : {lsNum}',
    '\nSum : ' ,sum(lsNum)
)

#count
ls = [1,2,3,3,5,7,3,1,2,3]
print(
    f'\nls : {ls}',
    '\ncounting of 3 :',ls.count(3)
)
#reverse
ls.reverse()
print('\nReverse : ',ls)

#sort
lsunsorted = [5,7,3,1,2]
print('\nunsorted list :',lsunsorted)
lsunsorted.sort()
print('Sorted list :',lsunsorted)


print()