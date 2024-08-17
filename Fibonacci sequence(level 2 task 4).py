def fibonacci():                                      #function for fibonacci sequence
    n=int(input("Finonacci series upto terms "))        #taking input for number of terms
    n1=0
    n2=1
    if n==1: 
        print(n1)
    else:
        print(n1,n2,end=" ")
        for i in range(1,n+1):
            n3=n1+n2
            print(n3,end=" ")
            n1=n2
            n2=n3
           
fibonacci()
