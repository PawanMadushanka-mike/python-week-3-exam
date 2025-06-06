import random

while True:
    try:
        level=int(input("Level: "))
        if level>0:
            break
    except ValueError:
        pass

number=random.randint(1,level)

while True:
    try:
        guess=int(input("Guess: "))
        if guess<=0:
            continue
        elif guess<number:
            print("Too small!")
        elif guess>number:
            print("Too large!")
        else:
            print("just right!")
            break

    except ValueError:
        pass


        

