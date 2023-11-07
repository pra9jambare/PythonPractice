List = [10,23,24,42,642,21,2,23]

print("CurrentList ", List)

#Append
List.append(40)
print("After Append : ",List)

#insert
List.insert(1,100)
print("After Insert : ",List)

List2 = [100,200,300,500]
List.extend(List2)
print("After Extend : ",List)