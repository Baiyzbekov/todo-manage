from task_manager import TaskManager

tm = TaskManager("tasks.json")

while True:
    print("1. Show")
    print("2. Add")
    print("3. Delete")
    print("4. Exit")

    choice = input("Choose:")
    if choice == "1":
        print(tm.get_tasks())

    elif choice == "2":
        task = input("New task: ")
        tm.add_task(task)

    elif choice == "3":
        index = int(input("Number:  ")) - 1
        tm.delete_task(index)

    elif choice == "4":
        break