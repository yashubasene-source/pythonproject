num1 = int(input("enter number a: "))
num2 = int(input("enter number b: "))
num3 = int(input("enter number c: "))

if num1 > num2 and num1 > num3:
    print("largest number is :", num1 )
elif num2 > num1 and num2 > num3:
    print("largest number is :" , num2)
else :
    print("largest number is :" , num3)
    
