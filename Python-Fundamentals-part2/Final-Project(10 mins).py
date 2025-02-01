# Project Idea: Create a To-Do List Manager

# Requirements:
# Use a class 'ToDoList' with methods to add, remove, and view tasks.
# Save the tasks to a file.

# Example Implementation:

class ToDoList:
    def __init__(self):
        self.tasks = []  # Initialize an empty list to store tasks

    def add_task(self, task):
        self.tasks.append(task)  # Add a task to the list

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)  # Remove a task from the list if it exists

    def view_tasks(self):
        for task in self.tasks:
            print(f"- {task}")  # Print each task in the list

my_list = ToDoList()  # Create an instance of ToDoList
my_list.add_task("Learn Python")  # Add "Learn Python" to the task list
my_list.add_task("Write code")  # Add "Write code" to the task list
my_list.view_tasks()  # View all tasks in the list

# Challenge Students:

# Add functionality to save tasks to a file and load them when the program starts.
