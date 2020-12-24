# Hangman.py
import os

# Initialising Game Variables
user1 = "USER1"
user2 = "USER2"
playing = True
word = "HANGMAN"
guess_limit = 6
guess_count = 0
host = False

# Greet & Start
def start():
    print("")
    print("\t\t H A N G M A N")
    print("")
    print( "\t" + "\t  " + "_"*10)
    print( "\t" + "\t  | " + " "*7 + "|")
    print( "\t" + "\t  | " + " "*7 + "|")
    print( "\t" + "\t  O " + " "*7 + "|")
    print( "\t" + "\t/ | \\" + " "*6 + "|")
    print( "\t" + "\t / \\" + " "*7 + "|")
    print( "\t" + "\t" + " "*11 + "|")
    print( "\t" + "\t" + " "*11 + "|")
    print( "\t" + "_"*19 + "|")
    print("")

def take_word(word):
    guess_word = word
    if host:
        guess_word = input(user2 + " enter the word for the round : ")
    else:
        guess_word = input(user1 + " enter the word for the round : ")
    word = guess_word if guess_word else word
    return word

def screen_clear():
    if os.name == 'posix':
        _ = os.system("clear")
    else:
        _ = os.system("cls")

def game(guess_count):
    guess = ""
    used = []
    chars = list("_"*(len(word)))
    while (guess_count < guess_limit):
        # UPDATE SECTION
        print("")
        print("*"*20)
        print("YOUR PROGRESS \t \t : ", end=" ")
        for i in chars:
            print(i, end=" ")
        print("")
        print("No of Wrong guess \t : " + str(guess_limit - guess_count))
        print("Wrong guess limit\t : " + str(guess_limit))
        print("USED CHARACTERS \t \t : ", end=" ")
        for i in used:
            print(i.upper(), end=" ")
        print("")
        print("*"*20)

        # Taking Guess input
        guess = input("Enter a Character : ")
        if guess:
            guess_count += 1
        else:
            print("")
            print("")
            print("Guess Something")
            continue

        # Updating USED list
        if guess[0] in used:
            print("")
            print("")
            print("This Charcter is already used, try another one")
            guess_count -= 1
            continue
        else:
            used.append(guess[0])
        
        # Updatign CHAR list
        for i in range(len(word)):
            if word[i].lower() == guess[0].lower():
                chars[i] = word[i].upper()
        
        print(guess[0] in chars)
        if guess[0].upper() in chars:
            guess_count -= 1

        # If won then game ends
        if "_" in chars:
            pass
        else:
            break
    # UPDATE SECTION
    print("\n"*3)
    print("*"*20)
    print("YOUR PROGRESS \t \t : ", end=" ")
    for i in chars:
        print(i, end=" ")
    print("")
    print("No of Wrong guess \t : " + str(guess_limit - guess_count))
    print("Wrong guess limit\t : " + str(guess_limit))
    print("USED CHARACTERS \t \t : ", end=" ")
    for i in used:
        print(i.upper(), end=" ")
    print("")
    print("*"*20)
    print("")
    if (guess_limit == guess_count):
        winner = user2 if host else user1
        print(winner.upper() + " is the WINNER for the round")
    else:
        winner = user1 if host else user2
        print(winner.upper() + " is the WINNER for the round")
    print("")



if __name__ == "__main__":
    name = input("Enter the name for First User : ")
    user1 = name if name else user1
    name = input("Enter the name for Second User : ")
    user2 = name if name else user2
    while (playing):
        start()
        word = take_word(word)
        screen_clear()
        start()
        game(guess_count)
        play = input("Do You want to play another round : ")
        playing = True if play.lower() == "y" else False
        host = not(host)
        screen_clear()


