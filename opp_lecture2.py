class User:

    def __init__(self,username,userpass):
        self.__username = username
        self.userpass = userpass


    def editDetails(self):
        print('Enter Username')
        self.__username = input()
        print('Enter Password')
        self.userpass = input()

    def displayDetails(self):
        print('Username = ',self.__username)    
        print('Password = ',self.userpass)    


u1 = User('recimo','recimo123')
u1.__username='ddd'
# u1.displayDetails()
u1.editDetails()
u1.displayDetails()