def decide(n,x):
    if(n == "PAPER" and x == "STONE"):
        return 1
    elif(n == "SCISSOR" and x == "PAPER"):
        return 1
    elif (n == "STONE" and x == "SCISSOR"):
        return 1
    elif(n == "STONE" and x == "STONE"):
        return 2
    elif(n == "PAPER" and x == "PAPER"):
        return 2
    elif(n == "SCISSOR" and x == "SCISSOR"):
        return 2
    else:
        return 0

from random import choice
for i in range(1,11):
    x = input("Enter your choice: ")
    n = choice(("Paper","Stone","Scissor"))
    n = n.upper()
    print(n)
    M = decide(n,x.upper())
    if(M == 1):
        print("System win\n")
    elif(M == 2):
        print("Tie\n")
    else:
        print("You Win\n")

