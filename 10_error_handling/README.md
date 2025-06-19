# 🛡️ Module 10: Error Handling in Python

Errors can crash your program if not handled properly. Python gives us tools like `try` and `except` to **catch errors** and keep the program running smoothly.

---

## 🔍 1. What is an Error?

An error is something that stops your program from running.  
Common types:

- `SyntaxError` – Bad code structure  
- `ZeroDivisionError` – Dividing by zero  
- `ValueError` – Wrong type of data  
- `FileNotFoundError` – File doesn’t exist  
- `IndexError` – Accessing outside a list

---

## ✅ 2. Using try and except

```python
try:
    num = int(input("Enter a number: "))
    print(10 / num)
except:
    print("Something went wrong!")
```

This catches any error and prints a safe message.

## 🎯 3. Catching Specific Errors

You can catch specific types of errors:

```python
try:
    num = int(input("Enter a number: "))
    print(10 / num)
except ValueError:
    print("Please enter a number!")
except ZeroDivisionError:
    print("You can't divide by zero!")
```

## 🧹 4. Using finally

The `finally` block runs no matter what — even if there’s an error.

```python
try:
    file = open("data.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("File not found.")
finally:
    print("This block always runs.")
```

