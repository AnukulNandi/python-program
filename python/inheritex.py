class Members:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
        #firstname =input("Enter your first name") 
        #lastname =input("Enter your first name")
        
    
class Profile(Members):
    
    def printname(self):
        name = self.firstname +" "+ self.lastname
        print("your full name is " , self.firstname,self.lastname)
        print(name)
        
x= Profile("anukul","Nandi")
x.printname()
