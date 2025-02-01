# 🐍 **Python Fundamentals – Part 2 Teacher’s Guide for Jeff**

This guide continues from Part 1, delving deeper into Python with intermediate concepts, ensuring both you and your students build confidence in writing more complex code. Each section includes **what to say**, **step-by-step explanations**, **examples**, and **student activities**.

---

## 📚 **Class Plan Overview**
- **Objective:** Introduce intermediate Python concepts like advanced loops, file handling, error handling, and object-oriented programming.
- **Duration:** ~1 hour
- **Tools Needed:** Python installed on computers, IDLE, or an online Python editor (e.g., [Repl.it](https://repl.it)).
- **Outcome:** Students will understand file operations, exceptions, advanced loops, and the basics of classes and objects.

---

## 🔄 **1. Advanced Loops (10 mins)**

### 🗣️ **What to Say:**
*"Loops are powerful for repeating tasks, but they can do much more when combined with advanced techniques like nested loops and list comprehensions."*

### ✅ **Nested Loops:**
*"A loop inside another loop lets you work with grids or combinations."*

#### Example Code:
```python
for row in range(3):
    for col in range(3):
        print(f"({row}, {col})", end=" ")
    print()
```
**Output:**
```
(0, 0) (0, 1) (0, 2) 
(1, 0) (1, 1) (1, 2) 
(2, 0) (2, 1) (2, 2)
```

### ✅ **List Comprehensions:**
*"A shorthand way to create lists."*

#### Example Code:
```python
squares = [x**2 for x in range(5)]
print(squares)
```
**Output:** `[0, 1, 4, 9, 16]`

### 🛠️ **Student Activity:**
- Create a nested loop to print a 5x5 grid of numbers.
- Use a list comprehension to create a list of even numbers from 0 to 20.

---

## 📂 **2. File Handling (10 mins)**

### 🗣️ **What to Say:**
*"Python allows you to read, write, and update files easily. This is useful for saving data or working with external files."*

### ✅ **Key Methods:**
1. `open(filename, mode)` – Opens a file. Modes:
   - `'r'`: Read
   - `'w'`: Write (overwrites existing content)
   - `'a'`: Append
2. `read()` and `write()` – Read or write data.
3. Always close the file with `close()` or use `with`.

### ✅ **Example Code – Writing to a File:**
```python
with open("example.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("Python is fun!")
```

### ✅ **Example Code – Reading from a File:**
```python
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
```
**Output:**
```
Hello, World!
Python is fun!
```

### 🛠️ **Student Activity:**
- Write a program that asks the user for their name and saves it to a file.
- Read the file and display the saved name.

---

## 🐞 **3. Error Handling (10 mins)**

### 🗣️ **What to Say:**
*"Errors can crash programs, but Python’s `try-except` blocks help handle them gracefully."*

### ✅ **Basic Error Handling:**
#### Example Code:
```python
try:
    number = int(input("Enter a number: "))
    print(10 / number)
except ZeroDivisionError:
    print("You cannot divide by zero!")
except ValueError:
    print("Please enter a valid number!")
finally:
    print("Program finished.")
```

### 🛠️ **Student Activity:**
- Write a program that divides two numbers and handles invalid inputs or division by zero.

---

## 📦 **4. Introduction to Classes and Objects (20 mins)**

### 🗣️ **What to Say:**
*"Python is an object-oriented programming language. Classes are blueprints for creating objects, which are instances of these classes."*

### ✅ **Basic Class Example:**
```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says woof!")

my_dog = Dog("Buddy", 3)
print(my_dog.name)  # Output: Buddy
print(my_dog.age)   # Output: 3
my_dog.bark()       # Output: Buddy says woof!
```

### 🧠 **Explain Step-by-Step:**
1. `class Dog`: Defines the class.
2. `__init__`: A special method to initialize the object’s attributes.
3. `self`: Refers to the current object.
4. Methods like `bark()` define actions the object can perform.

### 🛠️ **Student Activity:**
- Create a class `Car` with attributes `brand` and `model`, and a method `drive()` that prints "The car is driving."
- Create an object of the `Car` class and call its methods.

---

## 🎓 **5. Final Project (10 mins)**

### 🛠️ **Project Idea:** Create a To-Do List Manager
1. **Requirements:**
   - Use a class `ToDoList` with methods to add, remove, and view tasks.
   - Save the tasks to a file.
2. **Example Implementation:**
```python
class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)

    def view_tasks(self):
        for task in self.tasks:
            print(f"- {task}")

my_list = ToDoList()
my_list.add_task("Learn Python")
my_list.add_task("Write code")
my_list.view_tasks()
```

### 🧠 **Challenge Students:**
- Add functionality to save tasks to a file and load them when the program starts.

---

## 🏁 **6. Wrap-Up and Q&A (5 mins)**

### 🗣️ **What to Say:**
*"You’ve taken your Python skills to the next level today! Great work on advanced loops, file handling, error handling, and even object-oriented programming."*

### 🧠 **Ask:**
- *“What was the most challenging part?”*
- *“What would you like to explore next?”*

---

Let me know if you'd like additional sections or further elaboration! 🚀
