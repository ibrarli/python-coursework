# 🧺 Module 5: Lists and Loops in Python

In this module, you’ll learn how to store multiple values in a single variable using **lists**, and how to loop through them.

---

## 📋 1. What is a List?

A **list** stores multiple items in one variable.

```python
fruits = ["apple", "banana", "mango"]
```
You can mix data types:

```python
mixed = [1, "hello", True]
```

## 🧠 2. Accessing Items

Use index numbers (starting from 0):

```python
fruits = ["apple", "banana", "mango"]
print(fruits[0])  # apple
print(fruits[2])  # mango
```

## ➕ 3. Adding and Changing Items

```python
fruits.append("orange")  # Adds to end
fruits[1] = "kiwi"       # Changes second item
```

## ❌ 4. Removing Items

```python
fruits.remove("apple")
fruits.pop()     # Removes last item
```

## 🔁 5. Looping Through a List

Using `for` loop:

```python
fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print(fruit)

```
Using `while` loop:

```python
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1
```

## 🔍 6. Useful List Functions

| Function         | Description                        |
|------------------|------------------------------------|
| `len(list)`      | Number of items in the list        |
| `list.append(x)` | Adds `x` to the end                |
| `list.remove(x)` | Removes first match of `x`         |
| `list.pop()`     | Removes last item                  |
| `list.sort()`    | Sorts the list                     |
| `list.reverse()` | Reverses the list order            |
