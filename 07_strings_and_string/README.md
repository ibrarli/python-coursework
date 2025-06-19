# 📝 Module 7: Strings and String Functions in Python

Strings are used to store text. In this module, you'll learn how to create, use, and manipulate strings in Python.

---

## 🔤 1. What is a String?

A **string** is a sequence of characters, written inside quotes.

```python
name = "Ibrar"
greeting = 'Hello'
```

## 🧠 2. String Indexing

Each character in a string has an index (starting from 0).


```python
text = "Python"
print(text[0])  # P
print(text[5])  # n
```
## 🔁 3. Loop Through a String

```python
for letter in "code":
    print(letter)
```

## ➕ 4. String Concatenation

Join strings using `+`:

```python
first = "Hello"
second = "World"
print(first + " " + second)
```

## 🎯 5. String Methods

Here are some useful string functions:

| Method                | Description                          |
|-----------------------|--------------------------------------|
| `len(text)`           | Length of the string                 |
| `text.lower()`        | Converts to lowercase                |
| `text.upper()`        | Converts to uppercase                |
| `text.strip()`        | Removes spaces from start & end      |
| `text.replace(x, y)`  | Replaces `x` with `y`                |
| `text.find(x)`        | Finds position of `x` in the string  |
| `text.split()`        | Splits string into a list            |

---

### 🔍 Example:

```python
message = "  Hello World  "
print(len(message))                      # 15
print(message.strip())                   # "Hello World"
print(message.lower())                   # "  hello world  "
print(message.replace("Hello", "Hi"))    # "  Hi World  "
```