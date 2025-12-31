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

print('\nThe string :',str5)
print('counting the i in string :',str5.count(char1))

#startwith and endwith
str6 = 'Hello python how are you'
string1 = 'Hello'
print('\nThe string :',str6)


print('\n')

