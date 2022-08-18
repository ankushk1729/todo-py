# Add utils file

from file_utils import get_file_data, write_to_file


class UserOperations:

#-------------------------------------------------------------------------------------
    def add_new_task(self, name):
        new_task = input("Enter the new task : ")
        new_dict = {
                    "task_name": new_task,
                    "Is_completed": False
                   }
        
        file_data = get_file_data()
        file_data[name]["tasks"].append(new_dict)

        write_to_file(file_data)

#------------------------------------------------------------------------------------- 

    def mark_task_as_done(self, name):
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

#-------------------------------------------------------------------------------------

    def list_all_tasks(self, user_name):
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
    

#-------------------------------------------------------------------------------------

    def list_all_completed(self, name):
        file_data = get_file_data()

        cnt = 1
        for i in file_data[name]["tasks"]:
            if i["Is_completed"] == True:
                print(cnt, end=") ")
                cnt += 1
                print(i["task_name"])

#-------------------------------------------------------------------------------------

    def list_all_Incompleted(self, user_index):
        file_data = get_file_data()

        cnt = 1
        for i in file_data[user_index]["tasks"]:
            if i["Is_completed"] == False:
                print(cnt, end=") ")
                cnt += 1
                print(i["task_name"])

#-------------------------------------------------------------------------------------

    