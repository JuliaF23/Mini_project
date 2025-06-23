# Empty list to store tasks
tasks = []

# Function to add a task
def add_task():
    task = input("Enter the task: ")  # Ask the user for the task
    tasks.append(task)  # Add task to the list
    print(f"'{task}' has been added to the list.")


# Loop for the menu
while True:
    print("\nTo-Do List Application")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Exit")

    # Ask the user for their choice
    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        print("You choose to remove a task:")
        if task in tasks:
            tasks.remove(task)
            print(f"'{task}' has been removed from the list.")
        else:
            print("Task not found.")
    elif choice == "3":
        print("You choose to view tasks.")
    elif choice == "4":
        print("Exiting the application.")
        break
    else:
        print("Invalid choice. Please try again.")


