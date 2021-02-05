import random
def hangman():
    
    word = random.choice(["india","america","finland","japan","newzealand"])
    valid = 'abcdefghijklmnopqrstuvwxyz'
    turns = 10
    guessmade = ""
    while True:
        main = ""
        missed = 0

        for letter in word:
            if letter in guessmade:
                main = main+letter
            else:
                main = main + "_" + " "

        if main == word:
            print(main)
            print("You Win!")
            break

        print("Guess the Word: ",main)
        guess = input()
        if guess in main:
            print("Don't write used character second time")
            print("Enter a Valid Character: ")
            guess = input()

        if guess in valid:
            guessmade = guessmade+guess
        else:
            print("Enter a Valid Character: ")
            guess = input()

        if guess not in word:
            turns = turns-1
            if turns == 9:
                print("1 time missed")
                print("9 turns left")
                print("--------")
            if turns == 8:
                print("2 time missed")
                print("8 turns left")
                print("--------")
                print("   O    ")
            if turns == 7:
                print("3 time missed")
                print("7 turns left")
                print("--------")
                print("   O    ")
                print("   |    ")
            if turns == 6:
                print("4 time missed")
                print("6 turns left")
                print("--------")
                print("   O    ")
                print("   |    ")
                print("  /     ")
            if turns == 5:
                print("5 time missed")
                print("5 turns left")
                print("--------")
                print("   O    ")
                print("   |    ")
                print("  / \   ")
            if turns == 4:
                print("6 time missed")
                print("4 turns left")
                print("--------")
                print("  \O    ")
                print("   |    ")
                print("  / \   ")
            if turns == 3:
                print("7 time missed")
                print("3 turns left")
                print("--------")
                print("  \O/   ")
                print("   |    ")
                print("  / \   ")
            if turns == 2:
                print("8 time missed")
                print("2 turns left")
                print("--------")
                print("  \O/|  ")
                print("   |    ")
                print("  / \   ")
            if turns == 1:
                print("9 time missed")
                print("1 turns left")
                print("Last breaths counting,Take care")
                print("--------")
                print("  \O_|/ ")
                print("   |    ")
                print("  / \   ")
            if turns == 0:
                print("You Lose")
                print("--------")
                print("   O_|  ")
                print("  /|\   ")
                print("  / \   ")
                break

name = input("Enter Your Name: ")
print("WELCOME", name.upper())
print("------------------------")
print("Try to guess in less than 10 attempts")
hangman()
print()
