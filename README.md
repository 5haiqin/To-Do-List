# 🔧 To-Do List Manager

A simple console-based To-Do List Manager written in Python. This application helps you organize tasks with features like adding, viewing, editing, deleting, and marking tasks as completed. All tasks are stored persistently in a `tasks.txt` file.

---

## 🗋 Features

- ✏️ **Add Tasks**: Add a task with a description and a deadline.
- 🔎 **View Tasks**: View all tasks, categorized as pending or completed.
- ✍️ **Edit Tasks**: Update the description or deadline of an existing task.
- ❌ **Delete Tasks**: Remove a task by its ID.
- 🚫 **Mark as Completed**: Change the status of a task from "Pending" to "Completed."
- 📂 **Persistent Storage**: Tasks are saved in a `tasks.txt` file for later use.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed on your system.

### Installation
1. Clone this repository or download the `main.py` file.
2. Ensure the `tasks.txt` file is in the same directory as `main.py`. If it doesn’t exist, the program will create it automatically.

---

## 🎨 Usage

### Running the Program
1. Open a terminal or command prompt.
2. Navigate to the directory containing `main.py`.
3. Run the script using:
   ```
   python main.py
   ```

### Application Menu
Upon running, you'll see the following menu:
```
Welcome to To-Do List Manager!
1. Add Task
2. View Tasks
3. Edit Task
4. Delete Task
5. Mark Task as Completed
6. Exit
```

### Example Workflow
#### 1. Add a Task
```
Enter task description: Complete the Python project
Enter deadline: 2024-12-31
Task added successfully!
```

#### 2. View Tasks
```
To-Do List:
[Pending]
1. Complete the Python project - Deadline: 2024-12-31

[Completed]
No tasks completed yet.
```

#### 3. Mark as Completed
```
Enter the task ID to mark as completed: 1
Task marked as completed!
```

#### 4. View Updated Tasks
```
To-Do List:
[Pending]
No pending tasks.

[Completed]
1. Complete the Python project - Completed
```

---

## 📂 File Structure

- **`main.py`**: The main Python script to run the application.
- **`tasks.txt`**: A text file used to store tasks persistently. Each task is stored in the format:
  ```
  Task ID,Description,Deadline,Status
  ```
  Example:
  ```
  1,Complete the Python project,2024-12-31,Completed
  ```

---

## 🛠️ Customization
- Change the file name for task storage by modifying the `TASKS_FILE` variable in the `main.py` file.
- Enhance the user interface with additional libraries like `colorama` for colored output.

---

## 🏆 Acknowledgments
- Inspired by the need for simple task management tools.
- Built as part of a learning project.

---

## 🙌 Contributions
Feel free to contribute by submitting issues or pull requests!
