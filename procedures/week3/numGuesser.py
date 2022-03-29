import random

rand = random.randint(0, 10000)
ans = -1

while(ans != rand):
  ans = int(input("Guess a number 0-10000: "))
  if(ans == rand):
    print("You win! The number was: " + str(rand))

  elif (ans > rand):
    print("The number is lower!")

  elif (ans < rand):
    print("The number is higher!")