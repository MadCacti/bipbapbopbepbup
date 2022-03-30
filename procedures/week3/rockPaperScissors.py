import random

answer = int(input("1 for Rock, 2 for Paper, 3 for Scissors "))

rand = random.randint(0,3)


if(answer == rand):
  print("TIE!")
elif(answer == 1 and rand == 3):
  print("ai chose scissors")
  print("YOU WIN!")
elif(answer == 1 and rand == 2):
  print("ai chose paper")
  print("YOU LOSE!")
  
elif(answer == 2 and rand == 1):
  print("ai chose rock")
  print("YOU WIN!")
elif(answer == 2 and rand == 3):
  print("ai chose scissors")
  print("YOU LOSE!")

elif(answer == 3 and rand == 1):
  print("ai chose rock")
  print("YOU LOSE!")
elif(answer == 1 and rand == 2):
  print("ai chose paper")
  print("YOU WIN!")
  