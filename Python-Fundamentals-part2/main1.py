# EXAMPLES NOT FOR USE
# --------------------

# Create a class called ToDoList
# The class should have the following methods:
# add_task(task) - This method should add a task to the list of tasks.
# remove_task(task) - This method should remove a task from the list of tasks.
# view_tasks() - This method should print all the tasks in the list.
# The class should have an attribute called tasks to store the list of tasks.
# The add_task() method should append the task to the tasks list.
# The remove_task() method should remove the task from the tasks list if it exists.
# The view_tasks() method should print each task in the tasks list.
# Create an instance of the ToDoList class.

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
# Output:
# - Learn Python
# - Write code
# The ToDoList class has three methods: add_task(), remove_task(), and view_tasks().
# The add_task() method appends a task to the tasks list.
# The remove_task() method removes a task from the tasks list if it exists.
# The view_tasks() method prints each task in the tasks list.
# An instance of the ToDoList class is created with the variable my_list.

# EXAMPLES NOT FOR USE
# --------------------
