import random

print("Welcome to Rock, Paper, Scissors Game")

def rockPaperScissor(playerPlay, pcPlay):
    if playerPlay == 0:
        if pcPlay == 0:
            print("The Computer chose ROCK \n\n Its a Draw")
        elif pcPlay == 1:
            print("The Computer chose PAPER \n\nYou Lose")
        else:
            print("The Computer chose SCISSOR \n\nYou Win, congratulations")
    elif playerPlay == 1:
        if pcPlay == 0:
            print("The Computer chose ROCK \n\nYou Win, congratulations")
        elif pcPlay == 1:
            print("The Computer chose PAPER \n\n Its a Draw")
        else:
            print("The Computer chose SCISSOR \n\nYou Lose")
    else:
        if pcPlay == 0:
            print("The Computer chose ROCK \n\nYou Lose")
        elif pcPlay == 1:
            print("The Computer chose PAPER \n\nYou Win, congratulations")
        else:
            print("The Computer chose SCISSOR \n\n Its a Draw")



playerPlay = int(input("Type 0 for Rock, 1 for Paper or 2 for Scissor\n"))
pcPlay = random.randint(0, 2)
print(f"{playerPlay} vs {pcPlay}")

rockPaperScissor(playerPlay, pcPlay)




