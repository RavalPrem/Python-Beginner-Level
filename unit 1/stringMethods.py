#string methods
str1 = 'This is first string 3'
print('\nThe actual string : ', str1)
print('lower : ', str1.lower())
print('upper : ', str1.upper())
print('capitalize : ', str1.capitalize())

print('\nmethods return in True or False (Boolean Data type)')
print('isupper :',str1.isupper())
print('islower :',str1.islower())
print('isdigit :',str1.isdigit())
print('isalnum :',str1.isalnum())
print('isspace :',str1.isspace())

#checking it is working or not
str2 = '12345'
print('\nthe string :', str2)
print('isdigit :',str2.isdigit())
print('isalnum :',str2.isalnum())

str3 = ' '
print('\nThe string :',str3)
print('isSpace :',str3.isspace())

str4 = 'Written string'
print('\nThe string :',str4)
print('length :',len(str4))


#counting the character that how many times it is appeared in the given string
str5 = 'This is string'
char1 = 'i'
#this is case sensitive

print('\nThe string :',str5)
print('counting the i in string :',str5.count(char1))

#count from given number position
print('Counting start from 4th index : ',str5.count(char1,4))


#startwith and endwith
str6 = 'Hello python how are you'
string1 = 'Hello'
print('\nThe string :',str6)
print('The string starts with Hello : ',str6.startswith(string1))
print('The string ends with You : ',str6.endswith('You')) #see it returns False because it is case sensitive

#using the find
str7 = 'python is programming language'
print('\nThe original String :',str7)
print('the word "is" starting position :',str7.find('is'))
print('can give the range :',str7.find('is',0,3)) #return -1 because can't find the "is" in given string

str8 = '    abc python abc       '
print('\nThe string : ',str8)
print('Using the strip :',str8.strip())
print('Using rstrip :',str8.rstrip('abc'))
print('Using lstrip :',str8.lstrip('abc'))

#swapping the case
str9 = "Hello Python"
print('\nThe string :',str9)
print('''Using the swapcase :''',str9.swapcase()) #string can also written in 3 invited comma
print('\n')