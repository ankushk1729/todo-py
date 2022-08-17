class AllChoice:
    def get_users_choice(self):
        print("Please enter the command number that you want to perform")
        print("Enter 1 to add new task")
        print("Enter 2 to mark task as done")
        print("Enter 3 to List all tasks")
        print("Enter 4 to list all the completed tasks")
        print("Enter 5 to list all the incompleted tasks")
        print("Enter 0 to exit")

        choice = input("Enter your choice : ")
        if choice.isdigit() and  (int(choice)>=0 and int(choice)<=5):
            return int(choice)
        print("Invalid choice, try again")
        print("-----------------------------------------------------------------")
        return int(self.get_users_choice())