age = int(input("Enter your age: "))
ticket_type = input("Enter ticket type (normal/premium): ").lower()

if ticket_type == "normal":
    price = 200

elif ticket_type == "premium":
    price = 350

else:
    print("Invalid Ticket Type")
    exit()

# Age ke according discount
if age < 5:
    discount = price
    final_price = 0

elif age <= 17:
    discount = price * 0.50
    final_price = price - discount

elif age <= 59:
    discount = 0
    final_price = price

else:
    discount = price * 0.30
    final_price = price - discount

print("Ticket Price: ₹", price)
print("Discount: ₹", discount)
print("Final Price: ₹", final_price)
