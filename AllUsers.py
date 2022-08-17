import json
import bcrypt
import Choices
import Operations
import maskpass
class User:
    
    def existing_user(self):
        name = input("Enter the user name, all smallcase : ")
        is_operation_successful=self.old_user(name)
        


    def add_new_user(self):
        self.add()


    def add(self):
        with open("user_data.json") as file_cursor:
            file_data = json.load(file_cursor)
        username = input("Enter the Username, all smallcase : ")
        username=username.lower()
        while username in file_data.keys():
            print("User already exists, try another username")
            username = input("Enter the Username : ")

        # print("Enter the password : ")
        password= maskpass.advpass()
        bytes = password.encode('utf-8')
        salt = bcrypt.gensalt()
        # Encrypt the stored pasword:
        hashed = bcrypt.hashpw(bytes, salt).decode()
        new_user_entry = {
            "password": hashed,
            "tasks": []
        }
        
        file_data[username] = new_user_entry
        with open("user_data.json", "w") as file_cursor:
            json.dump(file_data, file_cursor)

    def old_user(self, name):
        with open("user_data.json") as file_cursor:
            file_data = json.load(file_cursor)

        
        if not name in file_data.keys():
            print("No such user found...!")
            return False
        
        Password=maskpass.advpass().encode('utf-8')
        Tries = 2
        while not bcrypt.checkpw(Password, file_data[name]["password"].encode('utf-8')):
            if Tries == 0:
                print("ohho Incorrect Password, try again !!!")
                return False
            print(f'Invlaid Password, {Tries} left')
            Tries -= 1
            Password= maskpass.advpass().encode('utf-8')

        print("\nHello ", name, " : \n")

        user_choice=Choices.AllChoice()
        while True:
            user_command = user_choice.get_users_choice()
            
            all_operations = Operations.UserOperations()

            if user_command == 1:
                print("\n*****************Add New Task*****************************")
                all_operations.add_new_task(name)
                print("\n**********************************************************\n")


            elif user_command == 2:
                print("\n*******************Mark Task As Done**********************")
                all_operations.mark_task_as_done(name)
                print("\n**********************************************************\n")


            elif user_command == 3:
                print("\n******************List of all Tasks***********************")
                all_operations.list_all_tasks(name)
                print("\n**********************************************************\n")


            elif user_command == 4:
                print("\n*************List of all completed Tasks******************")
                all_operations.list_all_completed(name)
                print("\n**********************************************************\n")


            elif user_command == 5:
                print("\n***************List of all Incompleted Tasks**************")
                all_operations.list_all_Incompleted(name)
                print("\n**********************************************************\n")

                
            elif user_command == 0:
                return True
        