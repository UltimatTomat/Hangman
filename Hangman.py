import random
import time

print("Choose your category. The options are Food, Animals and Countries.")

while True:
    category = input().lower()
    if category == "animals":
        r = open("Animals.txt", "r")
        break
    elif category == "food":
        r = open("Food.txt", "r")
        break
    elif category == "countries":
        r = open("Countries.txt", "r")
        break
    else:
        time.sleep(.5)
        print("Sadly that isn't a category. The options are Food, Animals and Countries.")
time.sleep(.5)

File  = r.read()
List = list(map(str, File.split()))
OldWord = random.choice(List)
TheWord = OldWord
Lives = 10
PositionsList = []
ExtraPositionPoints = 0

print("This word contains", len(TheWord), "letters.")

while True:
    if TheWord == "":
        time.sleep(1)
        print("Congratulations, you won!")
        break
    time.sleep(.5)
    print("Guess a letter:")
    Letter = input().lower()
    if TheWord.find(Letter) != -1:
        NewWord = OldWord
        ExtraPositionPoints = 0
        PositionsList = []
        while True:
            if NewWord.find(Letter) == -1:
                break
            ExtraPositionPoints += 1
            Position = NewWord.find(Letter) + ExtraPositionPoints
            PositionsList.append(Position)
            NewWord = NewWord.replace(Letter, "", 1)
        time.sleep(.5)
        print("That's correct! It's the number/numbers", ', '.join(str(item) for item in PositionsList), "in the word.")
        TheWord = TheWord.replace(Letter, "")
    else:
        Lives -= 1
        if Lives == 9:
            time.sleep(.5)
            print("That's wrong.")
            time.sleep(.5)
            print("[///////// ]")
        elif Lives == 8:
            time.sleep(.5)
            print("That's wrong.")
            time.sleep(.5)
            print("[////////  ]")
        elif Lives == 7:
            time.sleep(.5)
            print("That's wrong.")
            time.sleep(.5)
            print("[///////   ]")
        elif Lives == 6:
            time.sleep(.5)
            print("That's wrong.")
            time.sleep(.5)
            print("[//////    ]")
        elif Lives == 5:
            time.sleep(.5)
            print("That's wrong.")
            time.sleep(.5)
            print("[/////     ]")
        elif Lives == 4:
            time.sleep(.5)
            print("That's wrong.")
            time.sleep(.5)
            print("[////      ]")
        elif Lives == 3:
            time.sleep(.5)
            print("That's wrong.")
            time.sleep(.5)
            print("[///       ]")
        elif Lives == 2:
            time.sleep(.5)
            print("That's wrong.")
            time.sleep(.5)
            print("[//        ]")
        elif Lives == 1:
            time.sleep(.5)
            print("That's wrong.")
            time.sleep(.5)
            print("[/         ]")
        else:
            time.sleep(.5)
            print("GAME OVER!")
            time.sleep(.5)
            print("The word was ", OldWord.upper(), ".", sep="")
            time.sleep(.5)
            break