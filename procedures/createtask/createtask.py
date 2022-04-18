import random

class Function:
    def __init__(self): # initial number
        self.numList = []
        self.guessThisNumber = random.randint(1,20)
        

    def __call__(self):  # main run sequence
        self.num = int(input("select a random number from 1-20: "))
        while self.num != self.guessThisNumber:
            print()
            print("Your number:", self.num)
            print("You need to get to:", self.guessThisNumber)
            self.numList.append(self.num)
            print("previous numbers:", self.numList)
            print("current score:", len(self.numList))
            self.functions()
        print("you got the right number! it was", self.guessThisNumber)
        print("you got it in", + len(self.numList) ,"tries")

    def functions(self):   # all functions to alter number
        print("Do you want to...")
        print()
        print("add a random amount from 1-9 (1)")
        print("subtract a random amount from 1-9 (2)")
        print("multiply by a random amount from 1-9 (3)")
        print("divide by a random amount from 1-9 (4)")
        print()
        userinput = int(input("input here: "))

        randNum = random.randint(1, 9)
        if userinput == 1:
            self.num = int(self.num) + int(randNum)
        elif userinput == 2:
            self.num = int(self.num) - int(randNum)
        elif userinput == 3:
            self.num = int(self.num) * int(randNum)
        elif userinput == 4:
            self.num = int(self.num) / int(randNum)
            self.num = round(self.num)
        else:
            print("Enter a number you goon")

fun = Function()

def driver():
    fun()

if __name__ == "__main__":
  driver()