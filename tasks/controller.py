import tasks.actions as actions


class Perform:
    def operation_type(user_command, name):
        all_operations = actions.UserOperations()
        
        match user_command:
            case 1:
                all_operations.add_new_task(name)


            case 2:
                all_operations.mark_task_as_done(name)


            case 3:
                all_operations.list_all_tasks(name)


            case 4:
                all_operations.list_all_completed(name)


            case 5:
                all_operations.list_all_Incompleted(name)

            case 0:
                return 0
            
            case _:
                return 0
