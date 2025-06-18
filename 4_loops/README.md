# 🔁 Module 4: Loops in Python

Loops help you repeat a task multiple times. Instead of writing the same code again and again, you can use a loop to do it for you.

---

## 🧠 1. The `for` Loop

A `for` loop is used when you know how many times you want to repeat something.

```python
for i in range(5):
    print("Hello")
```
This will print "Hello" 5 times.

### 👉 Example with numbers:

```python
for i in range(1, 6):
    print(i)
```

### Output:
```python
1
2
3
4
5
```
## 🔢 2. The `range()` Function

`range(start, stop)` gives a sequence of numbers.
- `range(5)` → 0 to 4
- `range(1, 6)` → 1 to 5
- `range(1, 10, 2)` → 1, 3, 5, 7, 9

## 🔄 3. The `while` Loop

A `while` loop repeats as long as the condition is `True`.

```python
count = 1

while count <= 5:
    print("Count:", count)
    count += 1
```

## 🛑 4. Loop Control: `break` and `continue`

- `break`: stop the loop
- `continue`: skip the current loop and go to the next

### 👉 Example:

```python
for i in range(1, 6):
    if i == 3:
        break
    print(i)
# Output: 1 2
```

```python
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
# Output: 1 2 4 5
```