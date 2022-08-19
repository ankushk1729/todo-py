import auth


class Main:

    def main_entry_loop(self):
        print("===============================================================")
        print("Enter 1 to Sign Up")
        print("Enter 2 to Sign In")
        print("Enter 0 to exit")

        entry_choice = input("Enter your choice : ")
        if entry_choice.isdigit() and  int(entry_choice) == 1:
            auth.Auth.sign_up()
        elif entry_choice.isdigit() and  int(entry_choice) == 2:
            auth.Auth.login()
        elif entry_choice.isdigit() and  int(entry_choice) == 0:
            exit()
        else:
            print("Invalid choice, try again...")
            



A = Main()
while True:
    A.main_entry_loop()
