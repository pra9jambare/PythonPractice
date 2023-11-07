num = int(input("Enter the number to check"))

if num % 3 == 0 :
    
    if num % 5 == 0 :
        
         if num % 10 == 0 :
              print("It is satisfying All the Condition")
         else:
              print("It is satisfying first & Second Condition but not third")
    else:
         print("It is satisfying first Condition but not 2nd")
else:
    print("Not Satisfying a single condition")