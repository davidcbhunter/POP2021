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
    


# let's test the distance function
position1 = Position(0,0)
position2 = Position(5,5)

#print(position1.Distance(position2))


# let's make a map - it will have a list of
# a list of positions
col = 10
row = col

Map = []
for y in range(row):
    r = []
    for x in range(col):
        #pos = Position(x,0)
        r.append("*")
    Map.append(r)

#Map[0][0] = "W"

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
        Map[self.position.y][self.position.x] = "*"
        self.position.x += pos.x
        self.position.y += pos.y
        Map[self.position.y][self.position.x] = "W"
        


wolf = Wolf(Position(1,8),"M",100,3)
print_map(Map)


command = ""
command = input("\n")
while command != "q":
# we can use W, A, S, D to move the wolf on the map
    if command == "w":
        #move up
        wolf.Move(Position(0,1))
    if command == "a":
        #move left
        wolf.Move(Position(-1,0))
    if command == "s":
        #move down
        wolf.Move(Position(0,-1))
    if command == "d":
        #move right
        wolf.Move(Position(1,0))
    print_map(Map)
    command = input("\n")






#Map[wolf.position.x][wolf.position.y] = "W"
