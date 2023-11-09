Color = {"Blue","Pink","Red"}
print("Color with no change",Color)

Color.add("Yellow")
print("Color afer adding",Color)

Color.remove("Pink")
print("Color afer adding",Color)

Days = {"Sunday","Monday","Friday"}

Color.update(Days)
print(Color)

#in delete if the word is not present it will throw error 
#bt in discard it will continue no matter it is present in set or not
Color.discard("Monday")
print(Color)
