price = 15.00
print("what you want big boy")
line = input().split("")

for i in line:
    if i == "T":
        price += 1.5
    elif i == "O":
        price += 1.25
    elif i == "P":
        price += 3.5
    elif i == "M":
        price += 3.75
    elif i == "A":
        price += 0.4

if price > 20:
    price *= 0.95

print(f"{price:.2f}")
