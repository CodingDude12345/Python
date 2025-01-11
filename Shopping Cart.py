item = input("what item are you buying?: ")
price = float(input("what is the price?: "))
quantity = int(input("how many?:"))

total = price * quantity

print(f"you have bought {quantity} {item}")
print(f"your total is: ${round(total, 2)}")