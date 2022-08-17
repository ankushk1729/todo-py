from datetime import datetime
import json
import datetime
class UserOperations:

#-------------------------------------------------------------------------------------
    def add_new_task(self, name):
        new_task = input("Enter the new task : ")
        new_dict = {
                    "task_name": new_task,
                    "Is_completed": False
                   }
        with open("user_data.json") as file_cursor:
            file_data = json.load(file_cursor)
        file_data[name]["tasks"].append(new_dict)
        file_cursor.close()
        with open("user_data.json", "w") as file_cursor:
            json.dump(file_data, file_cursor)

#------------------------------------------------------------------------------------- 

    def mark_task_as_done(self, name):
        self.list_all_tasks(name)
        task_number = int(input("Enter the task number to be marked as done : "))
        task_number -= 1
        file_cursor = open("user_data.json")
        file_data = json.load(file_cursor)
        while not (task_number in range(len(file_data[name]["tasks"]))):
            task_number = int(input("Invalid task number, try again.."))-1
        file_cursor.close()
        file_data[name]["tasks"][task_number]["Is_completed"] = True
        with open("user_data.json", "w") as file_cursor:
            json.dump(file_data, file_cursor)

#-------------------------------------------------------------------------------------

    def list_all_tasks(self, user_name):
        file_cursor = open("user_data.json")
        file_data = json.load(file_cursor)

        cnt = 1
        for i in file_data[user_name]["tasks"]:
            print(cnt, end=") ")
            cnt += 1
            print(i["task_name"], end=" : ")
            if i["Is_completed"] == True:
                print("Completed")
            else:
                print("InComplete")
        file_cursor.close()

#-------------------------------------------------------------------------------------

    def list_all_completed(self, name):
        file_cursor = open("user_data.json")
        file_data = json.load(file_cursor)

        cnt = 1
        for i in file_data[name]["tasks"]:
            if i["Is_completed"] == True:
                print(cnt, end=") ")
                cnt += 1
                print(i["task_name"])
        file_cursor.close()

#-------------------------------------------------------------------------------------

    def list_all_Incompleted(self, user_index):
        file_cursor = open("user_data.json")
        file_data = json.load(file_cursor)

        cnt = 1
        for i in file_data[user_index]["tasks"]:
            if i["Is_completed"] == False:
                print(cnt, end=") ")
                cnt += 1
                print(i["task_name"])
        file_cursor.close()

#-------------------------------------------------------------------------------------

    