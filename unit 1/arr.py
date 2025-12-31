#tuple (immutable datatypes means can't edit it's value)
tup1 = (1,3,'Raval Prem',2+3j)
print('the type of tup1 : ',type(tup1))

print('\nThe tuple down below \n',tup1, '\n')

'''
mutable datatype down below
all are similar to an array
'''
#list (values are in the [] brakets)
ls1 = [1,3,'string',1+2j, 'another string']
print('\nlist down below \n', ls1)
print('\n')

#dictionary (contains keys-pairs values)
person1 = {
    'name':'prem',
    'age':20,
    'course':'Bsc.It(Dual Specialization)'
}
print('\nDictionary down below \n', person1)
print('\n')

#set (values are in the {} brakets, it is unordered)
s1 = {1, 3.4, 'string', 'complex string', 3+4j, 'another string', 5}
print('\nset down below \n', s1)
print("\n")

'''
showing all datatyps of it
'''
print('\nType of tup1 : ', type(tup1))
print('\nType of ls1 : ', type(ls1))
print('\nType of person1 : ', type(person1))
print('\nType of s1 : ', type(s1))
print('\n')