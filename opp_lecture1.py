class Employee:

    def __init__(self):
        self.Name=''
        self.Address=''
        self.Salary=''
        self.Id=''

    def setDetails(self):
        print('Enter Emp ID')
        self.Id = input()
        print('Enter Name')
        self.Name = input()
        print('Enter Address')
        self.Address = input()
        print('Enter Salary')
        self.Salary = int(input())

    def getDetails(self):
        print(f'ID {self.Id}')
        print(f'Name {self.Name}')
        print(f'Address {self.Address}')
        print(f'Salary {self.Salary}')
        


irtiqa = Employee()
irtiqa.setDetails()
irtiqa.getDetails()