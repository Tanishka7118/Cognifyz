import random
def numberguess():
  print("Number Guesser...")
  start=int(input("Enter the lower range : "))
  end=int(input("Enter the upper range : "))
  print(f"Randomly a number is selected between {start} and {end} guess the number")           
  num = random.randint(start,end)                                                      #random is a built in module and .randint() function to select random number between specified limit
  while True:
    n=int(input(f"Your guess between {start} and {end} : "))
    if(num<n):
      print("To high!!!")
    elif(num>n):
       print("To low!!!")
    else:
       print("Winnn!!!")
       break
numberguess()