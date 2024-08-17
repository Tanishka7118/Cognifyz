def celsius(temp):                   #function to convert celsius to fahrenheight
    fahrenheight=(9/5)*temp + 32
    return fahrenheight                

def fahren(temp):                    #function to convert celsius to fahrenheight
    celsius=(temp-32)*5/9
    return celsius

temp=float(input("Temperature: "))                                                #taking temperature input 
unit=input(f"Temperature is in (c for celsius & f for fahrenheight): ")           #unit of temperature
if unit=="c":                                                                     #condition to check if temperature is in celsius
    print(f"The {temp} degree celsius in fahrenheight is ",celsius(temp))
elif unit=="f":                                                                   #condition to check if temperature is in celsius
    print(f"The {temp} fahrenheight in celsius is ",fahrenheight(temp))



