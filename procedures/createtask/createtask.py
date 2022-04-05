import random

numbers = []
randomNumber = random.randint(1,20)
numinput = input("select a random number from 1-20:")
run()

# seperate run code from whatever we do

def run(): # main run sequence

  if numinput != randomNumber:
    print("Your number:", numinput)
    print("You need to get to:", randomNumber)
    numbers.append(numinput)
    print("previous numbers:", numbers)
    functions(numinput)
    
  else:
    print("you got the right number! it was ", randomNumber)
    

def functions(numinput): # all functions to alter number
  print("Do you want to...")
  print("add a random amount from 1-9 (1)")
  print("subtract a random amount from 1-9 (2)")
  print("multiply by a random amount from 1-9 (3)")
  print("divide by a random amount from 1-9 (4)")
  function = input("Input here: ")
  if function == 1:
    numinput = numinput + random.randint(1,9)
  elif function == 2:
    
  