def Passwordchecker():                                                #function to check strength of password
    string=input("ENTER PASSWORD : ")                                 #taking pass as input
    lower=0
    upper=0
    digit=0
    others=0
    specialchar=0   
    if len(string)>=8:                                       #checking the length of password that it is greater than equal to 8 or not
        for ch in string:                                    #to check each character in string
            if ch.isupper():                                 #to check character is in upper case or not
                upper=upper+1
            elif ch.islower():                                 #to check character is in lower case or not
                lower=lower+1
            elif ch.isdigit():                                 #to check character is  digit or not
                digit=digit+1
            elif ch in "@*$#%?&":                              #to check character is in these following symbols or not
                specialchar=specialchar+1
        
    else:
        print("PASSWORD TOO SHORT")                            #if password len is less than 8
    
    if(upper>=1 and lower>=1 and digit>=1 and specialchar>=1):
        print("VERY STRONG")
    elif(upper>=1  and lower>=1 and  digit>=1 or upper>=1  and  lower>=1  and  specialchar>=1 or lower>=1  and  digit>=1  and  specialchar>=1 or upper>=1  and  digit>=1 and specialchar>=1):
        print("STRONG")
    elif(upper>=1 and lower>=1 or digit>=1 and specialchar>=1 or lower>=1 and digit>=1 or upper>=1 and digit>=1 or upper>=1 and specialchar>=1 or lower>=1 and specialchar>=1):
        print("MODERATRE")
    elif(upper>=1 or lower>=1 or digit>=1 or specialchar>=1):
        print("WEAK")
Passwordchecker()

    

