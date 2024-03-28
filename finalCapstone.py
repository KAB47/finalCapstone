import os
from datetime import datetime, timedelta
#

def register_user():
    # Function to register a new user
    username = input("Enter a new username: ")

    #check if user.txt file exists, create if not
    if not os.path.exists('user.txt'):
        with open('user.txt', 'w'):
            pass

    # Checking if username already exists
    with open('user.txt', 'r') as file:
        existing_users = [line.strip() for line in file.readlines()]

    if username in existing_users:
        print("Username already exists. Please choose a different username.")
        return

    with open('user.txt', 'a') as file:
        file.write(username + '\n')
    print(f"User '{username}' registered successfully.")


def add_task():
    # Function to add a new task
    # Implementation logic for adding a task
    pass


def view_tasks(tasks):
    # Function to view tasks assigned to the current user
    # Implementation logic for viewing user-specific tasks
    print("Tasks assigned to you:")
    for i, task in enumerate(tasks, start=1):
        completion_status = "Yes" if task["completed"] else "No"
        print(f"{i}. {task['description']} - Completed: {completion_status}, Due Date: {task['due_date']}")

    #get user input for task completion or editing
    user_input = input("Enter the task number to mark as complete/edit (or '-1' to return to the main menu): ")

    if user_input == '-1':
        return  # Return to the main menu

    try:
        task_index = int(user_input)
        if 1 <= task_index <= len(tasks):
            action = input("Enter 'c' to mark as complete, 'e' to edit the task: ")
            if action.lower() == 'c':
                tasks[task_index - 1]["completed"] = True
                print(f"Task {task_index} is marked as complete.")
            elif action.lower() == 'e':
                edit_task(tasks, task_index)
            else:
                print("Invalid action. Please enter 'c' to mark as complete or 'e' to edit the task.")
        else:
            print("Invalid task input. Please enter a valid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

    # Do not return to the main menu
    input("Press Enter to continue...")  # Wait for user input before continuing


def edit_task(tasks, task_index):
    # Function to edit a task
    # Implementation logic for editing a task
    try:
        if 1 <= task_index <= len(tasks):
            task = tasks[task_index - 1]

            if not task["completed"]:
                print(f"Editing Task {task_index}: {task['description']}")
                option = input("Enter 'u' to edit the username, 'd' to edit the due date, or 'c' to cancel: ")

                if option.lower() == 'u':
                    new_username = input("Enter the new username: ")
                    task["username"] = new_username
                    print("Username updated successfully.")
                elif option.lower() == 'd':
                    new_due_date = input("Enter the new due date (YYYY-MM-DD): ")
                    task["due_date"] = datetime.strptime(new_due_date, "%Y-%m-%d")
                    print("Due date updated successfully.")
                elif option.lower() == 'c':
                    print("Task editing canceled.")
                else:
                    print("Invalid option. Task editing canceled.")
            else:
                print("Completed tasks cannot be edited.")
        else:
            print("Invalid task index.")
    except ValueError:
        print("Invalid input. Please enter a valid task index.")


def generate_reports(tasks):
    # Function to generate reports
    # Implementation logic for generating reports

    total_tasks = len(tasks)
    completed_tasks = sum(task["completed"] for task in tasks)
    uncompleted_tasks = total_tasks - completed_tasks
    overdue_tasks = sum(1 for task in tasks if not task["completed"] and task["due_date"] < datetime.now())

    incomplete_percentage = (uncompleted_tasks / total_tasks) * 100 if total_tasks > 0 else 0
    overdue_percentage = (overdue_tasks / uncompleted_tasks) * 100 if uncompleted_tasks > 0 else 0

    with open('task_overview.txt', 'w') as task_file:
        task_file.write("Task Overview Report\n")
        task_file.write(f"Total Tasks: {total_tasks}\n")
        task_file.write(f"Completed Tasks: {completed_tasks}\n")
        task_file.write(f"Uncompleted Tasks: {uncompleted_tasks}\n")
        task_file.write(f"Overdue Tasks: {overdue_tasks}\n")
        task_file.write(f"Percentage of Incomplete Tasks: {incomplete_percentage:.2f}%\n")
        task_file.write(f"Percentage of Overdue Tasks: {overdue_percentage:.2f}%\n")

    print("Task overview report generated successfully.")


def main():
    # Sample tasks for testing
    tasks = [
        {"description": "Task 1", "completed": False, "due_date": datetime(2022, 3, 1)},
        {"description": "Task 2", "completed": False, "due_date": datetime(2022, 4, 15)},
        {"description": "Task 3", "completed": True, "due_date": datetime(2022, 2, 28)}
    ]

    # Main loop
    while True:
        print("Please select one of the following options:")
        print("r - Register User")
        print("a - Add Task")
        print("va - View All Tasks")
        print("vm - View My Tasks")
        print("gr - Generate Reports")
        print("ds - Display Statistics")
        print("e - Exit")

        user_input = input("Enter your choice: ")

        if user_input == 'r':
            register_user()
        elif user_input == 'a':
            add_task()
        elif user_input == 'va':
            view_tasks(tasks)
        elif user_input == 'vm':
            view_tasks(tasks)
        elif user_input == 'gr':
            generate_reports(tasks)
        elif user_input == 'ds':
            # Display statistics function (needs implementation)
            pass
        elif user_input == 'e':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()