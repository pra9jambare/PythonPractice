age = int(input("Enter the age "))

if age <= 0 or age >= 100:
    print("Invalid age")
elif age <= 18 or age <=75:
    print("You are allowed to work")
elif age < 18 or age <75:
    print("You are not allowed to work")
else :
    print("You are enough old to die")