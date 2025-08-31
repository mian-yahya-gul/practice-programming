class chatbook:
    def __init__(self): #constructor
        self.user_name = ''
        self.password = ''
        self.loggedin = False
        self.menu()


    def menu(self):
        user_input = input("""Welcome to chatbook!! How you would like to proceed?
                           1. Press 1 to signup
                           2. Press 2 to signin
                           3. Press 3 to write a post
                           4. Press 4 to message a friend
                           5. Press any other key to exit""")
        
        if user_input == "1":
            self.signup()
        elif user_input == "2": 
            self.sign_in()
        elif user_input == "3":
            self.my_post()
        elif user_input == "4":
            self.send_message() 
        else:
            exit()


    def signup(self):
        email = input("enter your email here -> ")
        pwd = input("setup your password here -> ")
        self.user_name = email
        self.password = pwd
        print("You have signed in successfully")
        print("\n")
        self.menu()


    def sign_in(self):
        if self.user_name == '' and self.password == '':
            print("Please SignUp first by pressing 1 in the Main Menu")
        else:
            uname = input("Please enter your email/username here -> ")
            pwd = input("setup your password here -> ")
            if self.user_name == uname and self.password == pwd:
                print("You have Signed in Successfully")
                self.loggedin=True
            else:
                print("Please enter the correct credentials")
        
        print("\n")
        self.menu()

    



    def my_post(self):
        if self.loggedin == True:
            txt = input("Please enter a message to post here -> ")
            print(f"following content has been posted {txt}")
        else:
            print("You need to loggedin to post something, Press 2 to loggedin")
        print("\n")
        self.menu()

    def send_message(self):
        if self.loggedin == True:
            txt = input("Please enter your message here -> ")
            frnd = input("please enter your friend name here -> ")
            print(f"Your message has been sent to {frnd}")
        else:
            print("You need to loggedin to post something, Press 2 to loggedin")
        print("\n")
        self.menu()



        


            





obj1 = chatbook()

     