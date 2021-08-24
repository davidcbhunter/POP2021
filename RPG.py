import time
import random
import winsound

class Enemy:
    def __init__(self,n,h,d):
        self.name = n
        self.hp = h
        self.damage = d


#We need a player class, too


slime = Enemy("Basic Slime", 10, 1)



command = ""

def ShowCommands():
    print("A is attack")
    print("D is defend")
    print("Q is quit")
    print("\n")

#the code below should repeat 10 times
ShowCommands()
command = input("Enter your command \n")

enemyChoice = random.randrange(1,4)
if enemyChoice == 1:
    #attack
    print("Attack")
    #if the enemy attacks, the player will take damage
    winsound.PlaySound("metal1.wav", winsound.SND_ASYNC)
elif enemyChoice == 2:
    #defend
    print("Defend")
    #if the enemy, defends it will not take damage
    winsound.PlaySound("metal2.wav", winsound.SND_ASYNC)
elif enemyChoice == 3:
    #runaway
    print("Run away")
    #if the enemy runs away, we should make a new enemy
    winsound.PlaySound("footstep.wav", winsound.SND_ASYNC)
time.sleep(1)

