price = float(input("Enter product price: ₹"))

if price <= 0:
    print("Invalid Price")

elif price >= 5000:
    discount_percent = 20

elif price >= 2000:
    discount_percent = 10

elif price >= 1000:
    discount_percent = 5

else:
    discount_percent = 0


discount = price * discount_percent / 100
final_price = price - discount

if price > 0:
    print("\nOriginal Price: ₹", price)
    print("Discount:", discount_percent, "%")
    print("Discount Amount: ₹", discount)
    print("Final Price: ₹", final_price)
