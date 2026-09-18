user = str(input("enter your choice : "))
computer = "rock"

if user == computer and computer == "rock":
    print("computer also rock :")
    print("it's Draw! : ")
elif user != computer :
    if user == "paper" and computer == "rock":
        print("computer is loss :")
        print("You Win :")   
    elif user == "seissors" and computer == "rock":
        print("computer is Win :")
        print("You loss :")
    else :
        print("invalid input plesse re enter the correct input: ")

