# 📘 Module 2: Python Basics – Variables, Data Types & Input

Welcome to Module 2! In this part, you’ll learn the core basics of Python such as variables, data types, taking input from the user, and using operators.

---

## 🧠 1. Variables

Variables are used to store information.

```python
name = "Ali"
age = 25
```

Rules:
- Variable names should not start with a number.
- Use letters, numbers, and underscores only.
- Be descriptive: user_age is better than x.

## 🔤 2. Data Types
Python has different types of data:


## 📋 Basic Data Types Table

| Type    | Description           | Example           |
|---------|------------------------|-------------------|
| `int`   | Whole numbers          | `10`, `-5`, `0`   |
| `float` | Decimal numbers        | `5.5`, `3.14`     |
| `str`   | Text (string) values   | `"Hello"`, `'abc'`|
| `bool`  | Boolean (True/False)   | `True`, `False`   |

---
### Check Data Type

You can use the `type()` function to check the type of any value or variable.

```python
x = 10
print(type(x))  # <class 'int'>

y = 3.14
print(type(y))  # <class 'float'>

z = "Hi"
print(type(z))  # <class 'str'>

flag = True
print(type(flag))  # <class 'bool'>
```

### Convert between types

```python
num_str = "10"
num = int(num_str)
```

## 3. User Input
Use input() to take user input (returns a string):
```python
name = input("Enter your name: ")
print("Hello, " + name)
```

if you want a number:
```python
age = int(input("Enter your age: "))
print("Next year, you will be", age + 1)
```

## 4. Operators
Arthimetic Operators:
```python
a = 10
b = 3

print(a + b)  # 13
print(a - b)  # 7
print(a * b)  # 30
print(a / b)  # 3.33
print(a % b)  # 1 (remainder)
print(a ** b) # 1000 (10^3)
print(a // b) # 3 (floor division)
```
Comparison Operators:
```python
print(a == b)  # False
print(a > b)   # True
```
## 5. Print Formatting
You can use `f-strings` to format output nicely:
```python
name = "Ali"
age = 25
print(f"My name is {name} and I am {age} years old.")
```

