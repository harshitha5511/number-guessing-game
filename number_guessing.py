
import random
secret = random.randint(1,100)
guess= int(input("guess the number:"))

while guess!=secret:
    if guess<secret:
        print("too low")
    elif guess>secret:
        print("too high")
        
    guess= int(input("try again:"))


print("correct")