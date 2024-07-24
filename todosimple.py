tasks = []

while True:
    print("\nMenu: \n1. Add task \n2. View tasks \n3. Remove task \n4. Exit")
    choice = input("What you like to do:")
    if choice == '1':
        tasks.append(input("Enter task:"))
    elif choice == '2':
        print("\nTasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    elif choice == '3':
        del tasks[int(input("Enter task number to be removed: ")) - 1]
    elif choice == '4':
        print("\nExited")
        break