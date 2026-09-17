a = int(input("enter a number : "))
b = int(input("enter a number : "))
c = int(input("enter a number : "))


if a >= b and a >= c :
    largest = a
elif b >= c and b >= a :
    largest = b
else :
    largest = c
print(largest)
