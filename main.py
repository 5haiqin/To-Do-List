import os

TASKS_FILE = "tasks.txt"

# Load tasks from the file
def load_tasks():
    tasks = []
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 4:
                    task = {
                        "id": int(parts[0]),
                        "description": parts[1],
                        "deadline": parts[2],
                        "status": parts[3]
                    }
                    tasks.append(task)
    return tasks

# Save tasks to the file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(f"{task['id']},{task['description']},{task['deadline']},{task['status']}\n")

# Display tasks in a readable format
def display_tasks(tasks):
    print("\nTo-Do List:")

    pending_tasks = [task for task in tasks if task["status"] == "Pending"]
    completed_tasks = [task for task in tasks if task["status"] == "Completed"]

    print("[Pending]")
    if pending_tasks:
        for task in pending_tasks:
            print(f"{task['id']}. {task['description']} - Deadline: {task['deadline']}")
    else:
        print("No pending tasks.")

    print("\n[Completed]")
    if completed_tasks:
        for task in completed_tasks:
            print(f"{task['id']}. {task['description']} - Completed")
    else:
        print("No tasks completed yet.")

# Main program
if __name__ == "__main__":
    tasks = load_tasks()

    while True:
        print("\nWelcome to To-Do List Manager!")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Edit Task")
        print("4. Delete Task")
        print("5. Mark Task as Completed")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":  # Add Task
            description = input("Enter task description: ").strip()
            deadline = input("Enter deadline: ").strip()

            if description and deadline:
                task_id = max([task["id"] for task in tasks], default=0) + 1
                new_task = {"id": task_id, "description": description, "deadline": deadline, "status": "Pending"}
                tasks.append(new_task)
                save_tasks(tasks)
                print("Task added successfully!")
            else:
                print("Description and deadline cannot be empty.")

        elif choice == "2":  # View Tasks
            display_tasks(tasks)

        elif choice == "3":  # Edit Task
            display_tasks(tasks)
            try:
                task_id = int(input("Enter the task ID to edit: ").strip())
                task = next((task for task in tasks if task["id"] == task_id), None)

                if task:
                    new_description = input(f"Enter new description (current: {task['description']}): ").strip()
                    new_deadline = input(f"Enter new deadline (current: {task['deadline']}): ").strip()

                    if new_description:
                        task["description"] = new_description
                    if new_deadline:
                        task["deadline"] = new_deadline

                    save_tasks(tasks)
                    print("Task updated successfully!")
                else:
                    print("Task ID not found.")
            except ValueError:
                print("Invalid input. Please enter a valid task ID.")

        elif choice == "4":  # Delete Task
            display_tasks(tasks)
            try:
                task_id = int(input("Enter the task ID to delete: ").strip())
                tasks = [task for task in tasks if task["id"] != task_id]
                save_tasks(tasks)
                print("Task deleted successfully!")
            except ValueError:
                print("Invalid input. Please enter a valid task ID.")

        elif choice == "5":  # Mark Task as Completed
            display_tasks(tasks)
            try:
                task_id = int(input("Enter the task ID to mark as completed: ").strip())
                task = next((task for task in tasks if task["id"] == task_id), None)

                if task and task["status"] == "Pending":
                    task["status"] = "Completed"
                    save_tasks(tasks)
                    print("Task marked as completed!")
                else:
                    print("Task ID not found or already completed.")
            except ValueError:
                print("Invalid input. Please enter a valid task ID.")

        elif choice == "6":  # Exit
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select an option from 1 to 6.")

