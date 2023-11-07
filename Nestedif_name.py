name = str(input("Enter the name "))
surname = str(input("Enter the surname "))

if name == "Pranav":
    print("First Name condition is matched")
    if surname == "Jambare":
        print("Name & Surname are matched")
    else:
        print("Sorry , Surname is not matching")
elif surname == "Jambare":
    print("Surname condition is matched")
else:
    print("Sorry NO match")