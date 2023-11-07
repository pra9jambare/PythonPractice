#Cost Price
CP_pen = int(input("Enter the Cost Price of PEN"))
CP_Compass = int(input("Enter the Cost Price of Compass"))
CP_Duster = int(input("Enter the Cost Price of Duster"))
CP_Bag = int(input("Enter the Cost Price of Bag"))

#Selling Price
SP_pen = int(input("Enter the Selling Price of PEN"))
SP_Compass = int(input("Enter the Selling Price of Compass"))
SP_Duster = int(input("Enter the Selling Price of Duster"))
SP_Bag = int(input("Enter the Selling Price of Bag"))

Total_CP = CP_pen + CP_Compass + CP_Duster + CP_Bag
Total_SP = SP_pen + SP_Compass + SP_Duster + SP_Bag

print("Total Cost Price is ",Total_CP,"\nTotal Selling Price is ",Total_SP)
Diff =  Total_SP - Total_CP
if Total_SP >= Total_CP :
    print("WoW !! We made a profit of rupees",Diff )
elif Total_SP <= Total_CP :
    print("Sorry !! We made a loss of rupees",Diff )
else:
    print("Invalid Number")