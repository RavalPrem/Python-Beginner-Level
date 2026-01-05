a = 1
while a <= 10:
    print(a, end=' ')
    a+=1

#break and continue keyword using
print('\n\n')
b = 1
while b <= 10:
    if b == 3:
        break
    print(b, end=' ')
    b+=1

print('\n\nUsing continue keyword')
c = 1
while c <= 11:
    if c == 5:
        c+=1 #we have to incremented this value otherwise it will stuck at 5 and never executing the code
        continue
    print(c,end=' ')
    c+=1

