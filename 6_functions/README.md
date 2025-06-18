# 🧱 Module 6: Functions in Python

A **function** is a block of code that runs only when it's called. Functions help make code **reusable**, **organized**, and **easy to manage**.

---

## 🔧 1. Defining a Function

Use the `def` keyword to create a function.

```python
def greet():
    print("Hello, welcome!")
```

To run it, just call the function:

```python
greet()
```

## 🔧 2. Function with Parameters

You can pass `data` to a function using parameters.

```python
def greet(name):
    print("Hello,", name)
```

Call it with an argument:

```python
greet("Ali")  # Output: Hello, Ali
```

## 📤 3. Returning Values

Use `return` to send data back from a function.

```python
def add(a, b):
    return a + b

result = add(3, 5)
print(result)  # Output: 8
```

## 🔢 4. Default Parameter Values

You can set default values for parameters:

```python
def greet(name="Guest"):
    print("Hello,", name)

greet()           # Hello, Guest
greet("Ibrar")    # Hello, Ibrar
```

## ♻ 5. Why Use Functions?
- To avoid repeating code
- To organize logic into small parts
- To reuse the same code in different places