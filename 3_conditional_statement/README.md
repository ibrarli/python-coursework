# 📘 Module 3: Control Flow – Making Decisions in Python

In this module, you'll learn how to make decisions in your program using `if`, `elif`, and `else`. These control flow statements help your code respond to different situations.

---

## 🧠 1. The `if` Statement

Use `if` when you want to run some code only if a condition is `True`.

```python
age = 18

if age >= 18:
    print("You are an adult.")
```

##  2. The else Statement

Use `else` to run a block of code if the `if` condition is `False`.

```python
age = 15

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
```

## 🔁 3. The elif Statement

Use `elif` (else if) to check multiple conditions.

```python
marks = 75

if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
else:
    print("Grade: F")
```

## 🔐 4. Logical Operators

You can combine conditions using logical operators:

|Operator |	Meaning	           | Example                         |
|---------|--------------------|---------------------------------|
|and      |	Both must be true  | `if age > 18 and citizen:`      |
|or       |	One must be true   | `if age > 18 or has_permission:`|
|not      |	Reverse condition  | `if not is_banned:`             |


## 🔍 5. Comparison Operators

| Operator | Description        | Example   |
|----------|--------------------|-----------|
| `==`     | Equal to           | `x == 5`  |
| `!=`     | Not equal to       | `x != 5`  |
| `>`      | Greater than       | `x > 5`   |
| `<`      | Less than          | `x < 5`   |
| `>=`     | Greater or equal   | `x >= 5`  |
| `<=`     | Less or equal      | `x <= 5`  |

