# Simple tasks list App

tasks = []  # list to store tasks

def show_menu():
    print("\n===== TASKS LIST MENU =====")
    print("1. Add a new task")
    print("2. Show all tasks")
    print("3. Delete a task")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        task = input("Enter a new task: ")
        tasks.append(task)
        print(f" Task '{task}' added.")

    elif choice == "2":
        print("\nYour tasks:")
        if not tasks:
            print("No tasks yet!")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "3":
        print("\nChoose a task to delete:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
        try:
            index = int(input("Task number to delete: ")) - 1
            if 0 <= index < len(tasks):
                removed = tasks.pop(index)
                print(f" Task '{removed}' deleted.")
            else:
                print("Invalid number.")
        except ValueError:
            print("Please enter a valid number.")

    elif choice == "4":
        print("see you soon!")
        break

    else:
        print("Invalid choice, please try again.")
