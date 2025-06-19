# 📁 Module 9: File Handling in Python

File handling allows your program to read and write data to files like `.txt` files. This is useful for saving user data, logs, or reports.

---

## 📂 1. Opening a File

Use the `open()` function:

```python
file = open("example.txt", "r")  # Open for reading
```


### 📂 File Modes

| Mode | Description                      |
|------|----------------------------------|
| `r`  | Read (default)                   |
| `w`  | Write (overwrites file)          |
| `a`  | Append (add to file)             |
| `x`  | Create (error if file exists)    |

---

## 📝 2. Reading from a File

```python
file = open("data.txt", "r")
content = file.read()
print(content)
file.close()
```
You can also read line by line:

```python
for line in open("data.txt", "r"):
    print(line)
```

## ✍ 3. Writing to a File

```python
file = open("output.txt", "w")
file.write("Hello, this is a new file.\n")
file.close()
```
⚠ Note: `"w"` will overwrite the file if it already exists.

## ➕ 4. Appending to a File

```python
file = open("output.txt", "a")
file.write("This line is added at the end.\n")
file.close()
```

## ✅ 5. Using `with` Statement

This is the best way to work with files. It auto-closes the file.

```python
with open("output.txt", "r") as file:
    print(file.read())
```