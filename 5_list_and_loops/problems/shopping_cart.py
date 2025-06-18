cart = []

for i in range(5):
    item = input(f"Enter item {i+1}: ")
    cart.append(item)

print("Your Shopping Cart:")
for item in cart:
    print("-", item)
