Color = {"Purple","Blue","Pink","Red"}
Days = {"Sunday","Monday","Friday"}
Color1 = {"Blue","Pink","Red","White","Black","Yellow"}
print("Color with no change",Color)

#in delete if the word is not present it will throw error 
#bt in discard it will continue no matter it is present in set or not
Color.discard("Monday")
print(Color)

#when you want to print two different set
print(Color,Days)
Together = Color.union(Days)
print(Together)

#we can do same thing with update
Color.update(Days)
print("Two Sets in one",Color)

#Duplicate values
Color.intersection_update(Color1)
print("Common Values are",Color)

#Only unique from Color1
Color.symmetric_difference_update(Color1)
print("Unique Values are",Color)