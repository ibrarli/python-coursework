# 📦 Module 8: Python Collections – List vs Tuple vs Set vs Dictionary

Python provides built-in collection types to store multiple values. Each one has a specific use case.

---

## 📋 1. List – Ordered & Changeable

A **list** can store multiple items in order. It can be changed (mutable).

```python
fruits = ["apple", "banana", "mango"]
fruits.append("orange")
print(fruits[0])  # apple
```
✅ Allows duplicates
✅ Items can be changed
✅ Ordered

## 🔒 2. Tuple – Ordered & Unchangeable
A tuple is like a list, but it cannot be changed after creation.

```python
numbers = (1, 2, 3)
print(numbers[1])  # 2
```
❌ Cannot add or remove items
✅ Ordered
✅ Faster than lists

## 🚫 3. Set – Unordered & Unique
A set stores items in no particular order and removes duplicates automatically.

```python
colors = {"red", "green", "blue", "red"}
print(colors)  # {'red', 'green', 'blue'}
```
❌ No duplicates
❌ Unordered (no indexing)
✅ Fast lookup
✅ Used for unique data

## 🗂️ 4. Dictionary – Key-Value Pairs

A dictionary stores data as key-value pairs.

```python
person = {
    "name": "Ali",
    "age": 25
}
print(person["name"])  # Ali
```
✅ Fast access by key
✅ Keys must be unique
✅ Values can be anything

## 🧠 Summary Table

| Type        | Ordered | Changeable | Duplicates   | Indexing    | Example Syntax         |
|-------------|---------|------------|--------------|-------------|------------------------|
| List        | ✅ Yes  | ✅ Yes     | ✅ Yes       | ✅ Yes      | `["a", "b", "c"]`       |
| Tuple       | ✅ Yes  | ❌ No      | ✅ Yes       | ✅ Yes      | `("a", "b", "c")`       |
| Set         | ❌ No   | ✅ Yes     | ❌ No        | ❌ No       | `{"a", "b", "c"}`       |
| Dictionary  | ✅ Yes  | ✅ Yes     | ✅ Keys No   | ✅ By Key   | `{"name": "Ali"}`       |

