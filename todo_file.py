# todo_file.py

import os

FILE_NAME = "tasks.txt"

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            tasks = [line.strip() for line in f.readlines()]
        return tasks
    return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        for task in tasks:
            f.write(task + "\n")

def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks yet!")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def main():
    tasks = load_tasks()
    print("=== Simple To-Do List (File-Based) ===")
    
    while True:
        print("\nOptions:")
        print("1. Add task")
        print("2. View tasks")
        print("3. Delete task")
        print("4. Quit")
        
        choice = input("Choose an option (1-4): ").strip()
        
        if choice == "1":
            task = input("Enter task: ").strip()
            if task:
                tasks.append(task)
                save_tasks(tasks)
                print(f"Task added: {task}")
            else:
                print("Task can't be empty.")
        
        elif choice == "2":
            show_tasks(tasks)
        
        elif choice == "3":
            show_tasks(tasks)
            try:
                num = int(input("Enter task number to delete: "))
                if 1 <= num <= len(tasks):
                    removed = tasks.pop(num - 1)
                    save_tasks(tasks)
                    print(f"Deleted task: {removed}")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Enter a valid number.")
        
        elif choice == "4":
            print("Goodbye!")
            break
        
        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main()