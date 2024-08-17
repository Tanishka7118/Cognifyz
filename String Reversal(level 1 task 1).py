def reverse(string):                           #function to reverse a string
    rev=" "
    for i in string:
        rev=i+rev
    return rev

string=input("Enter the string: ")              #taking input of string
print("Reversed string: ",reverse(string))      #reversed string
