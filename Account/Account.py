class AMS:
    def __init__(self):
        # Created some initiaters for the system
        self.fname = ""
        self.lname = ""
        self.dob = ""
        self.mobno = 0
        self.gmail = ""
        global P
        global a
        self.pawd = ""

    # Account Creation for new user
    def account_creation(self):
        print("----------- ***************** --------------")
        self.fname = input("Enter your Firstname: ")
        self.lname = input("Enter your Lastname: ")
        self.dob = input("Enter your Date of Birth: ")
        self.mobno = int(input("Enter your Mobile Number: "))
        a = input("Enter your Valid G-Mail: ")
        self.gmail = a.lower()
        p = input("Create a Password: ")
        while len(p) <= 8:
            print("------ Password must contain 8 characters -----")
            p = input("Create a Password: ")
        self.pawd = input("Confirm Password: ")
        while self.pawd != p:
            print("---- OOPS ! Password doesn't match -----")
            self.pawd = input("Confirm Password: ")
        if self.pawd == p:
            print("Password created successfully")
        print("---- ** ! Account has been created Successfully ! ** ----")
        print("----------- ***************** --------------")

    # Log-in to the Account
    def login_account(self):
        print("----------- ***************** --------------")
        a = input("Enter your G-Mail: ".lower())
        self.lgmail = a
        P = input("Enter your Password: ")
        self.lpawd = P
        if (self.lgmail == self.gmail) and (self.lpawd == self.pawd):
            print("Login Successfully")
        else:
            print("Failure !")
        print("----------- ***************** --------------")
        
    # Account Profile 
    def account_profile(self):
        print("----------- ***************** --------------")
        print(f"Username: {self.fname} {self.lname}")
        print("Your Date of Birth: ",self.dob)
        print("Your Mobile Number: ",self.mobno)
        print("Your Gmail: ",self.gmail)
        print("Your Password: ",self.pawd)
        print("----------- ***************** --------------")


    # Main Function
    def main(self):
        msg = "1. Account Creation \n"
        self.account_creation()
        self.account_profile()

gr = AMS()
gr.main()