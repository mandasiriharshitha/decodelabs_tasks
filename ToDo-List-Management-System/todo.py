tasks = []
next_id = 1

while True:

    print("\n" + "=" * 40)
    print("       TO-DO LIST MANAGEMENT")
    print("=" * 40)

    print("1. Add Task")
    print("2. View Tasks")
    print("3. Search Task")
    print("4. Update Task Status")
    print("5. Delete Task")
    print("6. Exit")

    choice = input("\nEnter Your Choice: ")

    # ADD TASK
    if choice == "1":

        task_name = input("Enter Task Name: ").strip()

        if task_name == "":
            print("Task Name Cannot Be Empty!")
            input("\nPress Enter To Continue...")
            continue

        task = {
            "id": next_id,
            "title": task_name,
            "status": "Pending"
        }

        tasks.append(task)
        next_id += 1

        print("Task Added Successfully!")
        input("\nPress Enter To Continue...")

    # VIEW TASKS
    elif choice == "2":

        if len(tasks) == 0:
            print("No Tasks Available!")

        else:
            print("\n========== TASK LIST ==========")
            print(f"Total Tasks: {len(tasks)}\n")

            for task in tasks:
                print(
                    f"ID: {task['id']} | "
                    f"Task: {task['title']} | "
                    f"Status: {task['status']}"
                )

        input("\nPress Enter To Continue...")

    # SEARCH TASK
    elif choice == "3":

        keyword = input("Enter Task Name to Search: ").lower()

        found = False

        for task in tasks:

            if keyword in task["title"].lower():

                print(
                    f"ID: {task['id']} | "
                    f"Task: {task['title']} | "
                    f"Status: {task['status']}"
                )

                found = True

        if not found:
            print("Task Not Found!")

        input("\nPress Enter To Continue...")

    # UPDATE TASK
    elif choice == "4":

        try:

            task_id = int(input("Enter Task ID: "))

            found = False

            for task in tasks:

                if task["id"] == task_id:

                    task["status"] = "Completed"

                    print("Task Marked as Completed!")

                    found = True
                    break

            if not found:
                print("Task ID Not Found!")

        except ValueError:
            print("Please Enter a Valid Number!")

        input("\nPress Enter To Continue...")

    # DELETE TASK
    elif choice == "5":

        try:

            task_id = int(input("Enter Task ID to Delete: "))

            found = False

            for task in tasks:

                if task["id"] == task_id:

                    tasks.remove(task)

                    print("Task Deleted Successfully!")

                    found = True
                    break

            if not found:
                print("Task ID Not Found!")

        except ValueError:
            print("Please Enter a Valid Number!")

        input("\nPress Enter To Continue...")

    # EXIT
    elif choice == "6":

        print("\nThank You!")
        print("Project Closed Successfully.")
        break

    # INVALID CHOICE
    else:

        print("Invalid Choice! Please Try Again.")
        input("\nPress Enter To Continue...")
