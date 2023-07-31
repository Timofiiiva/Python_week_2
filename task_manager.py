tasks = []


def show_menu():
    print("\n=== Task Manager ===")
    print("1. View current tasks")
    print("2. Add a new task")
    print("3. Mark a task as completed")
    print("4. Delete a task")
    print("5. Exit")


def view_tasks():
    if not tasks:
        print("\nNo tasks found.")
    else:
        print("\nCurrent task list:")
        for index, task in enumerate(tasks, start=1):
            status = "completed" if task["completed"] else "not completed"
            print(f"{index}. [{status}] {task['name']}")


def add_task():
    name = input("\nEnter the task name: ")
    tasks.append({"name": name, "completed": False})
    print(f'\nTask "{name}" added successfully!')


def mark_completed():
    view_tasks()
    choice = int(
        input("\nChoose a task to mark as completed (enter the task number): ")
    )
    if 1 <= choice <= len(tasks):
        tasks[choice - 1]["completed"] = True
        print(f"Task \"{tasks[choice - 1]['name']}\" marked as completed!")
    else:
        print("Invalid choice. Please try again.")


def delete_task():
    view_tasks()
    choice = int(input("\nChoose a task to delete (enter the task number): "))
    if 1 <= choice <= len(tasks):
        deleted_task = tasks.pop(choice - 1)
        print(f"Task \"{deleted_task['name']}\" deleted.")
    else:
        print("Invalid choice. Please try again.")


def main():
    print("Welcome to the Task Manager!")
    while True:
        show_menu()
        choice = input("\nEnter your choice: ")

        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            mark_completed()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("\nExiting the Task Manager. Have a nice day!")
            break
        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()
