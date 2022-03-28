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