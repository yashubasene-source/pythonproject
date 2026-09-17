a = float(input("enter your first number : "))
b = float(input("enter your second number : "))


operator = input("enter your operator (+,-,*,/) : ")


if operator == '+':
    result = a+b
elif operator == '-' :
    result = a-b
elif operator == '*' :
    result = a*b
elif operator == '/' :
    if b == 0 :
        result = ("cannot divide by the zero ")
    else :
        result = a/b
else :
     result = "Error: Invalid operator"

print("Result : " ,result)
