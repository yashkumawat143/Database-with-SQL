import sys
from app import ap   
class Flipkart:
    def __init__(self):
        self.db = ap()
        self.menu()

    def menu(self):
        user = input("""
        1. Enter 1 to Register
        2. Enter 2 to Login
        3. Anything else to Exit
        """)

        if user == "1":
            self.register()
        elif user == "2":
            self.login()
        else:
            sys.exit(1000)

    def register(self):
        name=input("Enter the name : ");
        email=input("Enter the email : ");
        password=input("Enter the password : ");
        res=self.db.registor(name,email,password);
        if res:
            print("Registration successful")
        else:
            print("registration fail");
        self.menu();

    
    

    def login(self):
        email=input("Enter the email ");
        password=input("Enter the password ");
        data=self.db.search(email,password);
        if len(data)==0:
            print("Incorrect email/password")
            self.login();
        else:
            print("Hello",data[0][1]);


obj = Flipkart()