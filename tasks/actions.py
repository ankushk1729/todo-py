from datetime import datetime

from config.constants import NEW_LINE_SEPARATOR
from data.utils import get_file_data, write_to_file


class UserOperations:

#-------------------------------------------------------------------------------------
    def add_new_task(self, name):
        print("\n*****************Add New Task*****************************\n")
        new_task = input("Enter the new task : ")
        deadline = input("Please enter the task deadline in format DD/MM/YY HH:MM ")
        new_dict = {
                    "task_name": new_task,
                    "Is_completed": False,
                    "deadline":deadline
                   }
        
        file_data = get_file_data()
        file_data[name]["tasks"].append(new_dict)

        write_to_file(file_data)
        print(NEW_LINE_SEPARATOR)

#------------------------------------------------------------------------------------- 

    def mark_task_as_done(self, name):
        print("\n*******************Mark Task As Done**********************")
                
        if self.list_all_tasks(name) == False:
            print("No tasks entered, please enter a task first!")
            return
        task_number = int(input("Enter the task number to be marked as done : "))
        task_number -= 1
        file_data = get_file_data()
        while not (task_number in range(len(file_data[name]["tasks"]))):
            task_number = int(input("Invalid task number, try again.."))-1
        file_data[name]["tasks"][task_number]["Is_completed"] = True
        
        write_to_file(file_data)
        print(NEW_LINE_SEPARATOR)

#-------------------------------------------------------------------------------------

    def list_all_tasks(self, user_name):
        print("\n******************List of all Tasks***********************")
                
        file_data = get_file_data()
        if len(file_data[user_name]["tasks"])==0:
            return False

        cnt = 1
        for i in file_data[user_name]["tasks"]:
            print(cnt, end=") ")
            cnt += 1
            print(i["task_name"], end=" : ")
            if i["Is_completed"] == True:
                print("Completed")
            else:
                print("InComplete")
    
        print(NEW_LINE_SEPARATOR)

#-------------------------------------------------------------------------------------

    def list_all_completed(self, name):
        print("\n*************List of all completed Tasks******************")
                
        file_data = get_file_data()

        cnt = 1
        for i in file_data[name]["tasks"]:
            if i["Is_completed"] == True:
                print(cnt, end=") ")
                cnt += 1
                print(i["task_name"])
        print(NEW_LINE_SEPARATOR)

#-------------------------------------------------------------------------------------

    def list_all_Incompleted(self, user_name):
        print("\n***************List of all Incompleted Tasks**************")
                
        file_data = get_file_data()

        cnt = 1
        for i in file_data[user_name]["tasks"]:
            if i["Is_completed"] == False:
                print(cnt, end=") ")
                cnt += 1
                print(i["task_name"])

        print(NEW_LINE_SEPARATOR)
#-------------------------------------------------------------------------------------

    def show_unfinished_tasks(self, user_name):
        print("\n***************List of all unfinished Tasks**************")

        file_data = get_file_data()
        format_data = "%d/%m/%y %H:%M"
        cnt = 1
        for i in file_data[user_name]["tasks"]:
            current_date = datetime.now()
            if datetime.strptime(i["deadline"], format_data) < current_date and i["Is_completed"] == False: 
                print(cnt, end=") ")
                cnt += 1
                print(i["task_name"])

        print(NEW_LINE_SEPARATOR)
