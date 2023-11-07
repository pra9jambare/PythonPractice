Value = str(input("Enter the message "))

#Range
for x in range(0, 5):
    print(Value)

#List
Fruit_List = ["apple", "banana", "cherry"]

for x in Fruit_List:
    print("Color is",x)

#Breakstatement
Fruit_List = ["apple", "banana", "cherry"]

for x in Fruit_List:
    if x == "banana":
        break
    else:
        print("Color is",x)

#ContinueStatement
Fruit_List = ["apple", "banana", "cherry"]

for x in Fruit_List:
    if x != "banana":
        print("Color is ",x)
        continue
    else:
        break

