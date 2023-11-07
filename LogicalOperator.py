num1=int(input("Enter the number1 "))
num2=int(input("Enter the number2 "))

exp1 = num1 > num2
exp2 = num2 == num1 

print("check AND", exp1 and exp2)
print("check OR",exp1 or exp2)
print("check NOT",not(exp1))
