import AllUsers

class MainClass:

    def main_entry_loop(self):
        print("===============================================================")
        print("Enter 1 to Sign Up")
        print("Enter 2 to Sign In")
        print("Enter 0 to exit")

        user_obj=AllUsers.User()
        entry_choice = input("Enter your choice : ")
        if entry_choice.isdigit() and  int(entry_choice) == 1:
            user_obj.add_new_user()
        elif entry_choice.isdigit() and  int(entry_choice) == 2:
            user_obj.existing_user()
        elif entry_choice.isdigit() and  int(entry_choice) == 0:
            exit()
        else:
            print("Invalid choice, try again...")
            



A = MainClass()
while True:
    A.main_entry_loop()
