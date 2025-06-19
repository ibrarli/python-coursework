import string

password = "hello123@@"

digit_checker = any(char.isdigit() for char in password)
special_char_checker = sum(char in string.punctuation for char in password)

if len(password) < 8:
    print("Password must be at least 8 characters long.")
elif  not digit_checker:
    print("Password must contain at least one digit.")
elif special_char_checker < 2:
    print("Password must contain at least two special character.")  
else:
    print("Password is valid.")