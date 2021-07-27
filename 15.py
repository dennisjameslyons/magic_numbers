import random

#assigns a random number between 1 and 10 to the variable "magic_number"
magic_number = random.randint(1, 10)

def smaller_or_larger():

    while True:
        try:
            x = (int(input("enter a number please: ")))
            # y = int(x)
        except ValueError:
            print("Ever so sorry but I'm going to need a number.")
            continue
        else:
            break

    if x < magic_number:
        print("guess too small. guess some more.")
        return smaller_or_larger()
    elif x > 10:
        print("make sure your guess is smaller than 11.")
        return smaller_or_larger()
    elif x > magic_number:
        print("guess too great. try again, you'll get it.")
        return smaller_or_larger()
    else:
        print("Cherrio, you've done it, the magic number is yours! ")
        print(magic_number)

smaller_or_larger()
