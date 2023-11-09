Color = ("Blue","Pink","Red","Purple")

List = []

for x in reversed(Color):
    List.append(x)

NewColor = tuple(List)
print(NewColor)
print(type(NewColor))