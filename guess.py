
import random

secret =random.randint(1,5)

guess=0

while guess !=secret:

 guess = int(input("guess a numbar 1 and 5: "))

if guess >secret:
 print("too high! Try again.")
else:
 print("done guessing! you guessed the correct number.")
 