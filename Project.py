import datetime as dt

# Empty list to store tasks
tasks = []

# Function to add a task
def add_task():
    task = input("Enter the task: ")  # Ask for task name
    if task.strip() == "":
        print("The task is empty. Please try again.")
        return  # Stop this function if task is empty

    priority = input("Enter the priority (high, medium, low): ").strip().lower()
    deadline = input("Enter the deadline (YYYY-MM-DD): ").strip()

    # Save task as a dictionary
    task_info = {
        "name": task,
        "priority": priority,
        "deadline": deadline
    }

    tasks.append(task_info)  # Add task to the list

    # Confirm to the user
    print(f"'{task}' with priority '{priority}' and deadline '{deadline}' has been added to the list.")

# Function to suggest tasks
def suggest_task():
    suggest_tasks = []
    for task in tasks:
        # Skip when the deadline is not the expected data type
        try:
            date_deadline = dt.datetime.strptime(task["deadline"], "%Y-%m-%d").date()
        except:
            continue

        # Add to another list when the priority is high or it is within 7 days of the deadline
        today = dt.date.today()
        if date_deadline >= today and (task["priority"] == "high" or date_deadline <= today + dt.timedelta(days=7)):
            suggest_tasks.append(task)
    
    if not suggest_tasks:
        print("No suggestions for now. Enjoy the calm!")
    else:
        print("Here are some tasks you might want to work!")
    
    # Print the message by closest deadline
    suggest_tasks.sort(key=lambda task: task["deadline"])
    for task in suggest_tasks:
        print(f"{task["name"]} - {task["priority"]} - {task["deadline"]}")

# Create a loop for the menu
while True:
    print("\nAdvanced To-Do List Application")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Suggest Tasks")  
    print("5. Exit")
    
    # Ask the user for their choice
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_task()
    elif choice == "2":
        print("You chose to remove a task.")  
    elif choice == "3":
        print("You chose to view tasks.")  
    elif choice == "4":
        print("You chose to suggest tasks.")
        suggest_task()
    elif choice == "5":
        print("Exiting the application.")
        break
    else:
        print("Invalid choice. Please try again.")
