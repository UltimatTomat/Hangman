import random
import time
from slowprint.slowprint import *

while True:
    time.sleep(.5)
    print("Choose a category. The options are Food, Animals and Countries.")

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
    Again = 0
    Quit = 0
    Letters_Left = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    Underscores = len(TheWord)*"_"
    indexes = []
    indexes_left = []
    for z in range(len(OldWord)):
        indexes_left.append(z + 1)

    time.sleep(.5)
    print("The Word:")
    time.sleep(.5)
    for Character in Underscores:
        print("", Character, end="")
    print("")

    while True:
        if TheWord == "":
            time.sleep(.5)
            print("Congratulations, you won!")
            break
        time.sleep(.5)
        print("Guess a letter:")
        Letter = input().lower()
        if Letter not in Letters_Left:
            time.sleep(.5)
            print("This is either an invalid character or you've already guessed that letter.")
            continue
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
            for y in PositionsList:
                if y in indexes_left:
                    indexes.append(y - 1)
                    indexes_left.remove(y)
            new_character = Letter
            for i in indexes:
                Underscores = Underscores[:i] + new_character + Underscores[i+1:]
            time.sleep(.5)
            for character in Underscores:
                print("", character.upper(), end="")
            print("")
            Letters_Left.remove(Letter)
            TheWord = TheWord.replace(Letter, "")
            indexes = []
        else:
            Lives -= 1
            Letters_Left.remove(Letter)
            if Lives == 9:
                time.sleep(.5)
                print("That's wrong.")
                time.sleep(.5)
                print("         \n"
                    "  |        \n"
                    "  |        \n"
                    "  |        \n"
                    "  |        \n"
                    "  |        \n"
                    "  |        \n"
                    "============ ")
                time.sleep(.5)
                for character in Underscores:
                    print("", character.upper(), end="")
                print("")
            elif Lives == 8:
                time.sleep(.5)
                print("That's wrong.")
                time.sleep(.5)
                print("         \n"
                    "  |        \n"
                    "  |        \n"
                    "  |        \n"
                    "  |        \n"
                    "  |        \n"
                    " /|\       \n"
                    "============ ")
                time.sleep(.5)
                for character in Underscores:
                    print("", character.upper(), end="")
                print("")
            elif Lives == 7:
                time.sleep(.5)
                print("That's wrong.")
                time.sleep(.5)
                print("         \n"
                    "  |------  \n"
                    "  |        \n"
                    "  |        \n"
                    "  |        \n"
                    "  |        \n"
                    " /|\       \n"
                    "============ ")
                time.sleep(.5)
                for character in Underscores:
                    print("", character.upper(), end="")
                print("")
            elif Lives == 6:
                time.sleep(.5)
                print("That's wrong.")
                time.sleep(.5)
                print("         \n"
                    "  |------  \n"
                    "  |     |  \n"
                    "  |        \n"
                    "  |        \n"
                    "  |        \n"
                    " /|\       \n"
                    "============ ")
                time.sleep(.5)
                for character in Underscores:
                    print("", character.upper(), end="")
                print("")
            elif Lives == 5:
                time.sleep(.5)
                print("That's wrong.")
                time.sleep(.5)
                print("         \n"
                    "  |------  \n"
                    "  |     |  \n"
                    "  |     O  \n"
                    "  |        \n"
                    "  |        \n"
                    " /|\       \n"
                    "============ ")
                time.sleep(.5)
                for character in Underscores:
                    print("", character.upper(), end="")
                print("")
            elif Lives == 4:
                time.sleep(.5)
                print("That's wrong.")
                time.sleep(.5)
                print("         \n"
                    "  |------  \n"
                    "  |     |  \n"
                    "  |     O  \n"
                    "  |      \ \n"
                    "  |        \n"
                    " /|\       \n"
                    "============ ")
                time.sleep(.5)
                for character in Underscores:
                    print("", character.upper(), end="")
                print("")
            elif Lives == 3:
                time.sleep(.5)
                print("That's wrong.")
                time.sleep(.5)
                print("         \n"
                    "  |------  \n"
                    "  |     |  \n"
                    "  |     O  \n"
                    "  |     |\ \n"
                    "  |        \n"
                    " /|\       \n"
                    "============ ")
                time.sleep(.5)
                for character in Underscores:
                    print("", character.upper(), end="")
                print("")
            elif Lives == 2:
                time.sleep(.5)
                print("That's wrong.")
                time.sleep(.5)
                print("         \n"
                    "  |------  \n"
                    "  |     |  \n"
                    "  |     O  \n"
                    "  |    /|\ \n"
                    "  |        \n"
                    " /|\       \n"
                    "============ ")
                time.sleep(.5)
                for character in Underscores:
                    print("", character.upper(), end="")
                print("")
            elif Lives == 1:
                time.sleep(.5)
                print("That's wrong.")
                time.sleep(.5)
                print("         \n"
                    "  |------  \n"
                    "  |     |  \n"
                    "  |     O  \n"
                    "  |    /|\ \n"
                    "  |      \ \n"
                    " /|\       \n"
                    "============ ")
                time.sleep(.5)
                for character in Underscores:
                    print("", character.upper(), end="")
                print("")
            else:
                time.sleep(.5)
                print("         \n"
                    "  |------  \n"
                    "  |     |  \n"
                    "  |     O  \n"
                    "  |    /|\ \n"
                    "  |    / \ \n"
                    " /|\       \n"
                    "============ ")
                time.sleep(.5)
                slowprint("GAME OVER!", 1.5)
                time.sleep(.5)
                print("The word was ", end="")
                for char in  OldWord:
                    print(char.upper(), end="")
                print(".")
                time.sleep(.5)
                break
    
    time.sleep(.5)
    print("Type A to play agian, or E to exit.")
    while True:
        if input().lower() == "a":
            Again = 1
            break
        else:
            break
    if Again != 1:
        time.sleep(.5)
        print("Ok, bye...")
        time.sleep(1)
        break