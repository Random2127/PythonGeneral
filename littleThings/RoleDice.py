import random

# Options to choose from die or dice and how many faces it will have
# Basic role playing dice. 4/6/8/10/12/20/100

faceList = [4,6,8,10,12,20,100]

while True:
    print("The dices available are: 4/6/8/10/12/20/100\n")
    faces = input("How many faces do you want?")
    try:
        faces = int(faces)        
        if faces in faceList:
            die = random.randint(1,faces)
            print(f"{die}")
        else:
            print("Number chosen not available")
    except: 
        print("Wrong button!")

