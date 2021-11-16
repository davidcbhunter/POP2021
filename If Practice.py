import random

choices = ["Rock","Paper","Scissors"]


playerChoice = ""
playerScore = 0

computerChoice = ""
computerScore = 0

print("Let's play rock, paper, scissors!")
for x in range(1,4):
    computerChoice = choices[random.randint(0,2)]
    print("\n")
    playerChoice = input("Enter [R], [P], or [S] \n")
    #use if to see who won the match
