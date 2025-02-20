# Lesson 9
from random import choice
user = input("enter a choice of rock, paper or scissors: ")


cpu = choice(["rock", "paper","scissors"])
print(f"CPU choses {cpu}")

if user not in ["rock", "paper", "scissors"]:
    print("invalid choice")

else: 
    if (cpu == user):
        print("Tie")

    if (cpu == "rock"):
        if(user == "scissors"):
            print("CPU wins")
        else:
            print("You win")
    elif(user == "rock"):
        if(cpu == "paper"):
            print("CPU wins")
        else:
            print("You win")
