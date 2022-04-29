import random
import os

class Function:
    def __init__(self): # initial number
        self.numList = []
        self.Initial = int(input("Do you want to play on easy(1) or hard(2) mode? : "))
        if self.Initial == 1:
            self.guessThisNumber = random.randint(1,20)
        elif self.Initial == 2:
            self.guessThisNumber = random.randint(1,100)
        else:
            print("enter a number you fool")  # error code


    def __call__(self):  # main run sequence, this could be iterated differently, but makes more sense this way
        if self.Initial == 1:
            self.num = int(input("select a random number from 1-20: "))
            if self.num > 20 or self.num < 1: # error code
                print("that's outside the range!")
                exit()
            while self.num != self.guessThisNumber:
                print()
                print("Your number:", self.num)
                print("You need to get to:", self.guessThisNumber)
                self.numList.append(self.num)
                print("previous numbers:", self.numList)
                print("current score:", len(self.numList))
                option = 1  # helps set up different values of possible random math functions
                self.functions(option)

            print("you got the right number! it was", self.guessThisNumber)
            print("you got it in", + len(self.numList) ,"tries")


        elif self.Initial == 2:
            self.num = int(input("select a random number from 1-100: "))
            if self.num > 100 or self.num < 1: # error code
                print("that's outside the range!")
                exit()
            while self.num != self.guessThisNumber:
                print()
                print("Your number:", self.num)
                print("You need to get to:", self.guessThisNumber)
                self.numList.append(self.num)
                print("previous numbers:", self.numList)
                print("current score:", len(self.numList))
                option = 2  #  helps set up different values of possible random math functions
                self.functions(option)

            print("you got the right number! it was", self.guessThisNumber)
            print("you got it in", + len(self.numList) ,"tries")


    def functions(self, option):   # all functions to alter number
        if option == 1:  # sets different values for easy
            randNum = random.randint(1, 9)

        elif option == 2:  # sets different values for hard
            randNum = random.randint(1,20)

        print("Do you want to...")
        print()
        print("add by", randNum, "(1)")
        print("subtract by", randNum, "(2)")
        print("multiply by", randNum, "(3)")
        print("divide by", randNum, "(4)")
        print("go back to a previous number (5)")
        print()
        userinput = int(input("input here: "))
        os.system("clear") # clears screen for clarity


        if userinput == 1:
            self.num = int(self.num) + int(randNum)

        elif userinput == 2:
            self.num = int(self.num) - int(randNum)

        elif userinput == 3:
            self.num = int(self.num) * int(randNum)

        elif userinput == 4:
            self.num = int(self.num) / int(randNum)
            self.num = round(self.num)

        elif userinput == 5:
            print(self.numList)
            i = int(input("which number?"))
            self.num = self.numList[i-1]

        else:
            print("enter a number you fool")  # error code


fun = Function()

def driver():
    fun()


if __name__ == "__main__":
  driver()