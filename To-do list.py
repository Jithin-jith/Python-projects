import os

def load_tasks(filename="tasks.txt"):
    """Load tasks from a file."""
    if not os.path.exists(filename):
        return []
    with open(filename, "r") as file:
        return [line.strip() for line in file.readlines()]

def save_tasks(tasks, filename="tasks.txt"):
    """Save tasks to a file."""
    with open(filename, "w") as file:
        file.writelines([task + "\n" for task in tasks])

def display_tasks(tasks):
    """Display the to-do list."""
    if not tasks:
        print("No tasks available.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def main():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List Options:")
        print("1. Add Task")
        print("2. Update Task")
        print("3. Delete Task")
        print("4. Show Tasks")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            task = input("Enter task: ")
            tasks.append(task)
            save_tasks(tasks)
            print("Task added.")
        
        elif choice == "2":
            display_tasks(tasks)
            try:
                index = int(input("Enter task number to update: ")) - 1
                if 0 <= index < len(tasks):
                    new_task = input("Enter updated task: ")
                    tasks[index] = new_task
                    save_tasks(tasks)
                    print("Task updated.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
        
        elif choice == "3":
            display_tasks(tasks)
            try:
                index = int(input("Enter task number to delete: ")) - 1
                if 0 <= index < len(tasks):
                    tasks.pop(index)
                    save_tasks(tasks)
                    print("Task deleted.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
        
        elif choice == "4":
            display_tasks(tasks)
        
        elif choice == "5":
            print("Exiting To-Do List. Have a great day!")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()