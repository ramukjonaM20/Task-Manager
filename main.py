from task_manager import TaskManager

def main():
    manager = TaskManager()

    while True:
        print("\nTo-Do List Application")
        print("----------------------")
        print("1. Add Task")
        print("2. Edit Task")
        print("3. Delete Task")
        print("4. Mark Task Complete")
        print("5. Display Tasks")
        print("6. Quit")

        choice = input("Choose an option: ")

        if choice == '1':
            desc = input("Enter task description: ")
            manager.add_task(desc)
        elif choice == '2':
            manager.display_tasks()
            idx = int(input("Enter task number to edit: ")) - 1
            new_desc = input("Enter new description: ")
            manager.edit_task(idx, new_desc)
        elif choice == '3':
            manager.display_tasks()
            idx = int(input("Enter task number to delete: ")) - 1
            manager.delete_task(idx)
        elif choice == '4':
            manager.display_tasks()
            idx = int(input("Enter task number to mark complete: ")) - 1
            manager.mark_task_complete(idx)
        elif choice == '5':
            manager.display_tasks()
        elif choice == '6':
            print("Exiting To-Do List Application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
