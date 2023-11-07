Name = "Pranav"
Roll_no = 38
Age = 27.6
Indian = True
Criminal_Record = None

print ("Name of candidate is ",Name ,"\nRoll No of candidate is ",Roll_no,"\nAge of candidate is ",Age,"\ncandidate is Indian ?",Indian,"\nAny criminal records for associate",Criminal_Record)

#TypeError: can only concatenate str (not "int") to str
#print ("Name of candidate is " + Name + "\nRoll No of candidate is" + Roll_no + "\nAge of candidate is" + Age + "\ncandidate is Indian ?" + Indian + "\nAny criminal records for associate" + Criminal_Record)

#Expression in the print statement
print("My updated roll no is ",Roll_no + 2)

#Seprator in the print statement
print (Name ,Roll_no,Age,Indian,Criminal_Record, sep="-->")
print ("Name of candidate is ",Name ,"\nRoll No of candidate is ",Roll_no,"\nAge of candidate is ",Age,"\ncandidate is Indian ?",Indian,"\nAny criminal records for associate",Criminal_Record,sep="-->")


'''
print ("Name of candidate is ",Name)
print ("Roll No of candidate is ",Roll_no)
print ("Age of candidate is ",Age)
print ("candidate is Indian ?",Indian)
print ("Any criminal records for associate",Criminal_Record)
'''
print(type(Name),type(Roll_no),type(Age),type(Indian),type(Criminal_Record))
