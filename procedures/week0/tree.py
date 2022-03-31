import time
import os

height = int(input("enter a height: "))

stars = 1
for i in range(height):
    print((' ' * (height - i)) + ('*' * stars))
    stars += 2
print((' ' * height) + '|')
print()