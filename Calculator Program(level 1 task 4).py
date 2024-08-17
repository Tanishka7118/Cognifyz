n1=float(input("Enter number1:-"))  #Taking input for first number
n2=float(input("Enter number2:-"))  #Taking input for second number
print(" OPERATION ")                 #printing operation so user can choice desired operation
print("1: +")
print("2: -")
print("3: *")
print("4: /")
n=int(input("OPERATION NUMBER TO BE PERFORMED="))    #taking input of operation choice 
if n==1:                                              #conditions for performing operation
    res=n1+n2
elif n==2:
    res=n1-n2
elif n==3:
    res=n1*n2
elif n==4:
    res=n1/n2
else:
    print("Invalid choice")
print("Result:- ",res)                               #printing result
