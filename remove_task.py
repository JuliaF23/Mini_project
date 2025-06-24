def remove_task(tasks: list[str]) -> None:
    task = input("Enter the task to remove: ").strip()
    if task in tasks:
        tasks.remove(task)
        print(f"'{task}' has been removed from the list.")