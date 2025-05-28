def task():
    task = []
    print("---Welcome---")

    total_task = int(input("Enter The No. Of The Task You Want To Do: "))
    for i in range(1,total_task+1):
        task_name = input(f"Enter The {i} Task: ")
        task.append(task_name)
    print(f"Today Tasks Are{task}")
    while True:
        operation = int(input("Enter 1-Add\n2-Update\n3-View\n4-Delete\n5-Exit"))
        if operation == 1:
            task_Name = input("Enter The Task You Want To Add: ")
            task.append(task_Name)
        elif operation==2:
            updated_task = input("Enter The Task You Want To Update: ")
            if updated_task in task:
                update = input("Enter New Task: ")
                task.remove(updated_task)
                task.append(update)
            else:
                valid = input("Please!Enter Valid Task:")
        elif operation==3:
            print(f"Today Task Are {task}")
        elif operation == 4:
            delete = input("Enter The You Want To Delete: ")
            if delete in task:
                task.remove(delete)
                print("The Task Deleted")
            else:
                print("Please!Enter Valid Task: ")
        elif operation == 5:
            break
task()
