import random
def numberguess():                        
  print("Guessing Game...")
  print("Randomly a number is selected between 1 and 100 guess the number")
  num = random.randint(1,100)                                             #random is a built in module and .randint() function to select random number between specified limit
  while True:                                                              
    n=int(input("Your guess between 1 and 100: "))                       #taking a input of a number between 1 to 100
    if(num<n):
      print("To high!!!")
      print("Better luck next time.......!")
    elif(num>n):
       print("To low!!!")
       print("Better luck next time.......!")
    else:
       print("Winnn!!!")
       break
numberguess()