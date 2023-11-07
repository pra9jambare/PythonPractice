num = 1

for i in range (1,6):
    print(i * "*")

print (" -------XXX------")
num = 1

for i in range (1,6):
    print(i * "*")

j = 6
while j > 0:
    print(j * "*")
    j = j - 1 

print (" -------XXX------")

num_rows = int(input("Enter the number of rows"));
for i in range(0, num_rows):
	for j in range(0, num_rows-i-1):
		print(end=" ")
	for j in range(0, i+1):
		print("*", end=" ")
	print()