# To-Do List Manager

Welcome to the **To-Do List Manager**! 📝 This is a simple, console-based application to help you organize your tasks efficiently.

---

## 📖 Project Description
The To-Do List Manager allows users to:
- Add tasks with descriptions and deadlines.
- View all tasks categorized by status (Pending/Completed).
- Edit task details.
- Delete tasks.
- Mark tasks as completed.

All tasks are saved persistently in a file (`tasks.txt`), ensuring your data is safe across multiple sessions.

---

## ✨ Features Implemented

- **Add Tasks**: Input task description and deadline.
- **View Tasks**: See pending and completed tasks clearly categorized.
- **Edit Tasks**: Modify task details including description and deadline.
- **Delete Tasks**: Remove tasks from your to-do list.
- **Mark as Completed**: Update a task's status to completed.
- **File Handling**: Tasks are stored in `tasks.txt` for persistent storage.

---

## 🚀 How to Run the Project

1. **Clone the Repository**:
    ```bash
    git clone <repository-url>
    cd <repository-folder>
    ```

2. **Run the Script**:
    - Open a terminal in the project folder.
    - Execute the Python script:
      ```bash
      python todo_list_manager.py
      ```

3. Follow the console prompts to manage your tasks!

---

## 🛠 Instructions for Installation

1. Ensure **Python 3.x** is installed on your system. 🐍
   - Download Python: [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. Install the project dependencies (if any):
   ```bash
   pip install -r requirements.txt
   ```

   *(No external dependencies are currently required for this project.)*

3. Run the application as described above.

---

## 📝 Example Usage

### Main Menu:
```plaintext
Welcome to To-Do List Manager!
1. Add Task
2. View Tasks
3. Edit Task
4. Delete Task
5. Exit
Enter your choice: 1
```

### Adding a Task:
```plaintext
Enter task description: Complete the programming assignment
Enter deadline (YYYY-MM-DD): 2024-12-25
Task added successfully!
```

### Viewing Tasks:
```plaintext
To-Do List:
[Pending]
1. Complete the programming assignment - Deadline: 2024-12-25

[Completed]
No tasks completed yet.
```

### Marking as Completed:
```plaintext
Enter task number to mark as completed: 1
Task marked as completed!
```

---

## 🌟 Future Enhancements

- Add task sorting by deadline.
- Include a search/filter functionality.
- Implement a graphical user interface (GUI).

---

## 👏 Contributions

Feel free to contribute by submitting issues or pull requests!
