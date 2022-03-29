{% include base.html %}

# [Link to Replit](https://replit.com/@MadCacti/bipbapbopbepbup)

<iframe frameborder="0" width="100%" height="800px" src="https://replit.com/@MadCacti/bipbapbopbepbup?lite=true#README%22%3E">

## Week 0
### Learning how menus work and are built in terminal.
```
def menu():
    title = "menu" + banner 
    menu_list = main_menu.copy()
    menu_list.append(["patterns", submenu])
    buildMenu(title, menu_list)


```
## Week 1
### Learned how to create datalists and print them 3 different ways.

```
InfoDb = []

InfoDb.append({  
               "Name": "Raiden Tung",  
               "Birthday": "January 15",  
               "Classes Taking":["US History", "AM Lit", "AP Physics", "AP Stats", "AP CSP"]  
              })  

InfoDb.append({  
               "Name": "Audrey Zeng",  
               "Birth": "July 22",  
               "Classes Taking":["AP Studio Art","APEL","APUSH","AP Stats", "AP Bio"] 
              })

InfoDb.append({  
               "Name": "Jeffrey Lee",  
               "Birth": "December 27",  
               "Classes Taking":["AP Physics","AP Calc BC", "US History", "AM Lit", "AP Music Theory"] 
              })

InfoDb.append({  
               "Name": "Muhan Wei",  
               "Birth": "February 22",  
               "Classes Taking":["US History","Racquet Sports","Pre-Calc","AP Physics", "Offroll"] 
              })
```
```
def for_loop():
  for i in range(len(InfoDb)):
    print(InfoDb[i])

def while_loop(i=0):
  while i < len(InfoDb):
    print(InfoDb[i])
    i += 1

def recursive_loop(i=0):
  if i < len(InfoDb):
    print(InfoDb[i])
    recursive_loop(i+1)
```

## Week 2
### Created factorial, least common multiple, and palindrome functions.

Factorial:
```
class factorial:
  def __call__(self, num):
    final = 1
    for i in range(1, num + 1):
      final = final * i
    return final

factorial = factorial()
number = input("enter a number to find the factorial of: ")
number = int(number)
print("the factorial of ", number, "is",   factorial(number))
```
Least Common Multiple:
```
def lcm(num1, num2): # imperative
  if (num1 > num2):
    max = num1
  else:
    max = num2
  while (True):
      if (max % num1 == 0 and max % num2 == 0):
          break
      max = max + 1
  return max

class LCM:
  def __init__(self, num1, num2):
    self.num1 = num1
    self.num2 = num2

  def __call__(self):
    if self.num1 > self.num2:
      max = self.num1
      
    else:
      max = self.num2
    while (True):
      if (max % self.num1 == 0 and max % self.num2 == 0):
        break
      max = max + 1
    return max
    

def run():
	num = input("imperative(i) or OOP(o)")
	try:
		if num == 'i':
			print("the LCM of 12 and 30 is ", lcm(12,30))
		elif num == 'o':
			lcmoop = LCM(12,30)
			print("the LCM of 12 and 30 is ", lcmoop())
	except:
		print("that was not an option u old swine")


if __name__ == "__main__":
    run()
```
Palindrome:
```
class Palindrome:
    def __init__(self):
        self.index = 0
        self.input = ""
        self.specials = [" ", "-", ",", "!", "?", ".", "$", "*", "#", "%", "@", "`", "~", "<", ">", "{", "}", "[", "]"]

    def clean(self): # removes special characters and forces all characters to lower case
        self.input = self.input.lower()
        for element in self.specials:
            self.input = self.input.replace(element, '')
        return self.input

    def __call__(self, input):
        self.input = input
        print("original input:", self.input)
        self.clean()

        index = len(self.input)
        palindrome = True

        for i in range(index):
            if self.input[i] != self.input[::-1][i]: # ::-1 essentially reverses string and the rest compares each letter
                print("errors occurs at the pairs: " + str(i), str((len(self.input) - i)))
                palindrome = False

        if palindrome == False:
            print(self.input ,"is not a palindrome")
        else:
            print(self.input, " is a palindrome")


pal = Palindrome()
pal("racecar")
pal("wrineerw")
pal("raCe caR!>#")
```
