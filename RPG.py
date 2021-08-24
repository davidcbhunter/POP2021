import time
import random

class Enemy:
    def __init__(self,n,h,d):
        self.name = n
        self.hp = h
        self.damage = d


#We need a player class, too
# name, hp, damage, level, xp
class Player:
    def __init__(self,n,h,d,l,x):
        self.name = n
        self.hp = h
        self.damage = d
        self.level = l
        self.xp = x


slime = Enemy("Basic Slime", 10, 1)
player = Player("Tanjiro",100,2,1,0)


command = ""

def ShowCommands():
    print("A is attack")
    print("D is defend")
    print("Q is quit")
    print("\n")

#the code below should repeat 10 times
for x in range(10):
    ShowCommands()
    command = input("Enter your command \n")

    enemyChoice = random.randrange(1,4)
    if enemyChoice == 1:
        #attack
        #print("Attack")
        if command.lower() == "a":
            player.hp -= slime.damage
            slime.hp -= player.damage
        if command.lower() == "d":
            pass
        if command.lower() == "q":
            break
        #if the enemy attacks, the player will take damage
    elif enemyChoice == 2:
        #defend
        #print("Defend")
        if command.lower() == "a":
            pass
        if command.lower() == "d":
            pass
        if command.lower() == "q":
            break
        #if the enemy, defends it will not take damage
    elif enemyChoice == 3:
        #runaway
        print("Run away")
        
        #if the enemy runs away, we should make a new enemy
        slime = Enemy("New Enemy",random.ranrange(10,16),random.ranrange(2,5))
    time.sleep(1)
    print(player.name + " " + str(player.hp))
    print(slime.name + " " + str(slime.hp))
