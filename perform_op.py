import operations


class Perform:
    def operation_type(user_command, name):
        all_operations = operations.UserOperations()
        
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
            return 0
