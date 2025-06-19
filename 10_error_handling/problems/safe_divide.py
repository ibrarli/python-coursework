try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Result:", a / b)
except ValueError:
    print("Only numbers are allowed.")
except ZeroDivisionError:
    print("Second number can't be zero.")
