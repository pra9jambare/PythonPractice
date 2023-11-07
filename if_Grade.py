Marks = int(input("Enter the Marks "))

if Marks < 00:
    print("Invalid Marks")
elif Marks <= 35:
    print("You are a FAIL")
elif Marks <=50:
    print("You are JUST PASS")
elif Marks <= 80:
    print("You are Average")
elif Marks <= 95 :
    print("You are SCHOLAR")
else :
    print("You are GENIUS")