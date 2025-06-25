# Empty lists to store tasks
tasks = []
completed_tasks = []


# Function to add a task
def add_task():
    task = input("Enter the task: ").strip()
    if task == "":
        print("The task is empty. Please try again.")
        return

    priority = input("Enter the priority (high, medium, low): ").strip().lower()
    deadline = input("Enter the deadline (YYYY-MM-DD): ").strip()

    task_info = {
        "name": task,
        "priority": priority,
        "deadline": deadline
    }

    tasks.append(task_info)
    print(f"'{task}' with priority '{priority}' and deadline '{deadline}' has been added to the list.")

<<<<<<< completed_task
# Function to view tasks
def view_tasks():
    if not tasks:
        print("No pending tasks.")
    else:
        print("\nPending Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task['name']} (Priority: {task['priority']}, Deadline: {task['deadline']})")

# Function to view completed tasks
def view_completed_tasks():
    if not completed_tasks:
        print("No completed tasks.")
    else:
        print("\nCompleted Tasks:")
        for i, task in enumerate(completed_tasks, start=1):
            print(f"{i}. {task['name']} (Priority: {task['priority']}, Deadline: {task['deadline']})")

# Function to mark a task as completed
def mark_task_completed():
    if not tasks:
        print("No tasks to mark as completed.")
        return
    
    view_tasks()
    try:
        choice = int(input("Enter the number of the task to mark as completed: "))
        if 1 <= choice <= len(tasks):
            task = tasks.pop(choice - 1)
            completed_tasks.append(task)
            print(f"'{task['name']}' has been marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main menu loop
=======

# Function to view tasks
def view_tasks():
    print("Your tasks:")
    if not tasks:
        print("No tasks yet")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        if not tasks:
            print("You haven't completed any tasks yet.")


# Function to remove a task
def remove_task():
    task_name = input("Enter the task name to remove: ").strip()
    for task in tasks:
        if task["name"].lower() == task_name.lower():
            tasks.remove(task)
            print(f"'{task_name}' has been removed from the list.")
            return
    print(f"Task '{task_name}' not found.")


# Create a loop for the menu
>>>>>>> main
while True:
    print("\nAdvanced To-Do List Application")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Suggest Tasks")
<<<<<<< completed_task
    print("5. Mark Task as Completed")
    print("6. View Completed Tasks")
    print("7. Exit")
    
=======
    print("5. Exit")

    # Ask the user for their choice
>>>>>>> main
    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
<<<<<<< completed_task
        print("You chose to remove a task.") 
    elif choice == "3":
=======
        print("You chose to remove a task.")
        remove_task()
    elif choice == "3":
        print("You chose to view tasks.")
>>>>>>> main
        view_tasks()
    elif choice == "4":
        print("You chose to suggest tasks.")
    elif choice == "5":
        mark_task_completed()
    elif choice == "6":
        view_completed_tasks()
    elif choice == "7":
        print("Exiting the application.")
        break
    else:
        print("Invalid choice. Please try again.")
