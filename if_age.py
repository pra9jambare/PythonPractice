age = int(input("Enter the age "))

if age <= 0:
    print("Invalid age")
elif age <= 18:
    print("You are a KID")
elif age <=25:
    print("You are a TEEN")
elif age <= 50:
    print("You are a MAN")
elif age <= 100 :
    print("You are old")
else :
    print("You are enough old to die")