# we need the math library
# we need the random library
import math
import random


# let's make a position class
# it needs an x position and a y position
class Position:
    def __init__(self, xpos, ypos):
        self.x = xpos
        self.y = ypos
    
# it also needs a distance function:
# the distance function returns the distance
# to another position
    def Distance(self, pos):
        #find the distance in x and y
        dx = self.x - pos.x
        dy = self.y - pos.y

        #square the x and y distance
        dx = dx * dx
        dy = dy * dy

        #find the square root
        dist = math.sqrt(dx + dy)
        return dist


# let's make a map - it will have a list of
# of positions
col = 10
row = col

Map = []
for y in range(row):
    r = []
    for x in range(col):
        r.append("*")
    Map.append(r)


# let's print the map
def print_map(m):
    for r in reversed(m):
        s = ""
        for p in r:
            s += p
        print(s)


# let's make a wolf class - similar to the cat class
# it should have a position, energy, and age
# name - Lobo
class Wolf:
    def __init__(self,pos,gen, en = 100, ag = 3):
        self.name = "Lobo"
        self.position = pos
        self.age = ag
        self.gender = gen
        self.energy = en
        Map[pos.y][pos.x] = "W"
    def Move(self, pos):
        if self.position.y + pos.y >= len(Map) or \
        self.position.y + pos.y < 0:
            return
        if self.position.x + pos.x >= \
        len(Map[self.position.y + pos.y]) or \
        self.position.x + pos.x < 0:
            return
        # check energy!
        if self.energy - 3 < 0:
            return
        if self.position.x + pos.x == deer.position.x and \
           self.position.y + pos.y == deer.position.y:
            return
        # pos is inside the map, so we update self.position
        Map[self.position.y][self.position.x] = "*"
        self.position.x += pos.x
        self.position.y += pos.y
        Map[self.position.y][self.position.x] = "W"
        # add 0.1 to age
        self.age += 0.1
        # subtract 3 from energy
        self.energy -= 3
        # check distance between wolf and deer
        # if less than 2, print message "close!"
        if self.position.Distance(deer.position) < 2:
            print("close!")
        
# Let's make a deer class
# it should be similar to the Wolf class
class Deer:
    def __init__(self,pos,gen, en = 100, ag = 3):
        self.name = "Bambi"
        self.position = pos
        self.age = ag
        self.gender = gen
        self.energy = en
        Map[pos.y][pos.x] = "D"
    def Move(self, pos):
        if self.position.y + pos.y >= len(Map) or \
        self.position.y + pos.y < 0:
            return
        if self.position.x + pos.x >= \
        len(Map[self.position.y + pos.y]) or \
        self.position.x + pos.x < 0:
            return
        # check energy!
        if self.energy - 3 < 0:
            return
        # pos is inside the map, so we update self.position
        Map[self.position.y][self.position.x] = "*"
        self.position.x += pos.x
        self.position.y += pos.y
        Map[self.position.y][self.position.x] = "D"
        # add 0.1 to age
        self.age += 0.1
        # subtract 3 from energy
        self.energy -= 3


wolf = Wolf(Position(1,8),"M",100,3)
# print_map(Map)

# Let's make a deer
# Give it a random position on the map
deer = Deer(Position(random.randint(0,9), \
                     random.randint(0,9)),"F", \
            100, 3)


# show the map at the beginning
print_map(Map)

command = ""
command = input("\n")
while command != "q":
# we can use W, A, S, D to move the wolf on the map
    if command == "w":
        # move up
        wolf.Move(Position(0,1))
    if command == "a":
        # move left
        wolf.Move(Position(-1,0))
    if command == "s":
        # move down
        wolf.Move(Position(0,-1))
    if command == "d":
        # move right
        wolf.Move(Position(1,0))

    # show the map again
    print_map(Map)
    
    # get the next command from the player
    command = input("\n")
