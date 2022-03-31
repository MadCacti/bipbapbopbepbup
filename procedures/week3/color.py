def color(red, green, blue, text):
    return "\033[38;2;{};{};{}m{}\033[38;2;i".format(red, green, blue, text) # this weird string can basically just print it outs
  
red = input("add a value 0-255 for r:")
blue = input("add a value 0-255 for b:")
green = input("add a value 0-255 for g:")
text = "This is your colored text"

print(color(int(red), int(blue), int(green), text))
print()