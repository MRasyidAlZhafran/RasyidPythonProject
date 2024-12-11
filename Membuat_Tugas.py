def todo_list():
    tasks = []

    while True:
        action = input("Enter 'add' to add a task, 'view' to see tasks, or 'quit' to exit: ")

        if action == 'add':
            task = input("Enter the task: ")
            tasks.append(task)
            print(f"Task '{task}' added.")
        elif action == 'view':
            print("Your tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
        elif action == 'quit':
            break
        else:
            print("Invalid action.")

todo_list()