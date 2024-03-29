import random as R
class AMS:
    def __init__(self):
        # Created some initiators for the system
        self.fname = ""
        self.lname = ""
        self.dob = ""
        self.mobno = 0
        self.gmail = ""
        self.pawd = ""

    # Account Creation for a new user
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
        print("---- ** ! Account has been created Successfully ! ** ----")
        print("----------- ***************** --------------")

    # Log-in to the Account
    def login_account(self):
        print("----------- ***************** --------------")
        lgmail = input("Enter your G-Mail: ").lower()
        lpawd = input("Enter your Password: ")
        while lgmail != self.gmail or lpawd != self.pawd:
            print("---- ! OOPS your Gmail or Password is not matched ----")
            print("----- Please enter them correctly  -----")
            lgmail = input("Enter your G-Mail: ").lower()
            lpawd = input("Enter your Password: ")
        print("-- Login Successfully ! --")
        print("----------- ***************** --------------")

    # Change Password
    def change_password(self):
        print("----------- ***************** --------------")
        a = input("Enter your G-mail ID: ")
        if a == self.gmail:
            user_input = int(input("Please enter 1 to enter the Inbox: "))
            while user_input != 1:
                print("-- press one for enter in to the Inbox --")
                user_input = int(input("Please enter 1 to enter the Inbox: "))
            if user_input == 1:
                self.inbox()
                print("Plese enter your code for change the password")
                q = int(input("Enter your Code here: "))
                while q != self.code:
                    print("--- ! OOPS your code didn't matched, please enter it correctly ----")
                    q = int(input("Enter your Code here: "))
                if q == self.code:
                    p = input("Reset Password: ")
                    while len(p) < 8:
                        print("Password length must be above eight characters")
                        p = input("Reset Password: ")
                    self.pawd = input("Confirm Password: ")
                    while self.pawd != p:
                        print("--- Password not matched ! please enter it correctly ---")
                        self.pawd = input("Confirm Password: ")
                    print("Password Changed successfully")
                    print("----------- ***************** --------------")
        else:
            print("-- Please enter a Valid G-Mail ID --")
            print("----------- ***************** --------------")

    # Inbox for Change Password
    def inbox(self):
        print("----------- ***************** --------------")
        print("-------------- Inbox ----------------")
        print("------ ** Received New Message ** ------")
        c = R.randint(2356, 6658)
        self.code = c
        print("Your code for password change: ",self.code)
        print("----------- ***************** --------------")

    # Account Profile
    def account_profile(self):
        print("----------- ***************** --------------")
        print(f"Username: {self.fname} {self.lname}")
        print("Your Date of Birth: ", self.dob)
        print("Your Mobile Number: ", self.mobno)
        print("Your Gmail: ", self.gmail)
        print("Your Password: ", self.pawd)
        print("----------- ***************** --------------")

    # Main Function
    def main(self):
        msg = ("----------- ************* ------------- \n"
               "1. Account Creation \n"
               "2. Log-in \n"
               "3. Change Password \n"
               "4. Account Profile \n"
               "5. Exit \n"
               "------------ ************* ------------- \n")
        print(msg)
        while True:
            print(msg)
            user_choice = int(input("Enter Your Request: "))
            while user_choice not in [1, 2, 3, 4, 5]:
                print("---- ! OOPS Invalid Request ----")
                print(msg)
                user_choice = int(input("Enter Your Request in the above list: "))
            if user_choice == 1:
                self.account_creation()
            elif user_choice == 2:
                self.login_account()
            elif user_choice == 3:
                self.change_password()
            elif user_choice == 4:
                self.account_profile()
            elif user_choice == 5:
                print("----- BYE ! BYE ! ------")
                quit()


gr = AMS()
gr.main()
