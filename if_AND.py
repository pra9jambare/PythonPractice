English = int(input("Enter the English marks "))
Maths = int(input("Enter the Maths marks "))


if English > 75 and Maths > 75:
    print("You are EXCELLENT")
elif English > 75 and Maths < 75:
    print("You are good at English than Maths")
elif English < 75 and Maths > 75:
    print("You are good at Maths than English")
else :
    print("Invalid")