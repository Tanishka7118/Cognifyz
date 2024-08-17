def reverse(string):                           #function to reverse a string
    rev=""
    for i in string:
        rev=i+rev
    return rev

string=input("Enter the string : ")              #taking input of string
rev_string=reverse(string)
print("Reversed String : ",rev_string)
if string == rev_string :
    print("The string is Palindrome.")
else:
    print("The string is not Palindrome.")