import json
from rich import print

FILE_NAME = "tasks.json"

def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return[]

def save_tasks(tasks):
    with open (FILE_NAME, "w") as file:
        json.dump(tasks, file, inden=4)

def show_tasks(tasks):
    if not tasks:
        print("[red]No tasks found[/red]")
        return
        
    for i, task in enumerate(tasks, start=1):
        print(f"[green]{i}.[/green] [task]")

tasks = load_tasks()
while True:
    print("/n[bold blue]TODO MENU[/bold blue]")
    print("1. Show tasks")
    print("2. Add task")
    print("3. Delete task")
    print("4. Exite")

    choice = input("Choose:")
    if choice -- "1":
        show_tasks(tasks)
    elif choice == "2":
        task = input("New task: ")
        tasks.append(task)
        save_tasks(tasks)
    elif choice == "3":
        show_tasks(tasks)
        index = input(input("Task number:  ")) - 1

        if 0 <= index < len(tasks):
            tasks.pop(index)
            save_tasks(tasks)

    elif choice == "4":
        break



        