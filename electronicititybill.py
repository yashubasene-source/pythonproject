units = int(input("Enter electricity units: "))

if units < 0:
    print("Invalid Units")

elif units <= 100:
    bill = units * 5
    print("Your Electricity Bill: ₹", bill)

elif units <= 200:
    bill = units * 7
    print("Your Electricity Bill: ₹", bill)

elif units <= 300:
    bill = units * 10
    print("Your Electricity Bill: ₹", bill)

else:
    bill = units * 12
    print("Your Electricity Bill: ₹", bill)
    
