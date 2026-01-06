subject = ['DS','ES','AI','Python']
marks = [95,85,87,99]
print('\nPrint Subjects with there mark using for loop')

for s,m in zip(subject,marks):
    print(s,':',m)

print("\nprint the index number using enumerate")

for i,sub in enumerate(subject):
    print(i,':',sub)
    
print('\nAlso adding the starting index number in enumerate parameter')
for i,sub in enumerate(subject,start=10):
    print(i,':',sub)

print('\n')