List = [10,23,12,7,2,5,9,24,42,642,21,2,23]
print("CurrentList ", List)
newlist = []
newlist1 = [ num for num in List if num > 10 ]
for num in List:
    if num < 10:
        newlist.append(num)
        
print("We are with new list : ", newlist)
print("We are with new list1 : ", newlist1)

#Copy the exisitng list
ListCopy= List.copy()
print("It is a copy of List",ListCopy)

#adding two list
AddList = newlist + newlist1
print("Adding to list together", AddList)