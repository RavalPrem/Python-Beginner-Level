class messagePrint:
    print('Hello world')

Cobj = messagePrint()

class student:
    rno = 84
    name = 'prem'

    def printIt(self):
        print('\nThe rno : ',self.rno)
        print('The name : ',self.name)

student1 = student()
student1.printIt()

class emp:
    def empDetail(self,eid,ename):
        self.employeeid = eid
        self.employeename = ename
        
        print(f'\nEmployee id : {eid}')
        print(f'\nEmployee name : {ename}')

emp1 = emp()
print()
eid = int(input('Enter employee id : '))
ename = input('Enter employee name : ')

emp1.empDetail(eid,ename)

#python constructor
class consEx1:
    def __init__(self):
        print('\nPrinting from the consEx1 class constructor method')
ex = consEx1()
print()