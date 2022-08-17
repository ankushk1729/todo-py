import json

import bcrypt
import maskpass

import choices
import perform_op


class Auth:
    def login():
        name = input("Enter the user name, all smallcase : ")
        
        with open("user_data.json") as file_cursor:
            file_data = json.load(file_cursor)

        
        if not name in file_data.keys():
            print("No such user found...!")
            return False

        
        with open("user_data.json") as file_cursor:
            file_data = json.load(file_cursor)
        password=maskpass.advpass().encode('utf-8')
        tries = 2
        while not bcrypt.checkpw(password, file_data[name]["password"].encode('utf-8')):
            if tries == 0:
                print("Incorrect password, try again !!!")
                return False
            print(f'Invlaid password, {tries} left')
            tries -= 1
            password= maskpass.advpass().encode('utf-8')

        print("\nHello ", name, " : \n")
        
        while True:
            user_command = choices.AllChoice().get_users_choice()
            if user_command==0:
                return
            perform_op.Perform.operation_type(user_command, name)


    def sign_up():
        with open("user_data.json") as file_cursor:
            file_data = json.load(file_cursor)
        username = input("Enter the Username, all smallcase : ")
        username=username.lower()
        while username in file_data.keys():
            print("User already exists, try another username")
            username = input("Enter the Username : ")

        password= maskpass.advpass()
        bytes = password.encode('utf-8')
        salt = bcrypt.gensalt()
        
        hashed = bcrypt.hashpw(bytes, salt).decode()
        new_user_entry = {
            "password": hashed,
            "tasks": []
        }
        
        file_data[username] = new_user_entry
        with open("user_data.json", "w") as file_cursor:
            json.dump(file_data, file_cursor)
