import random
list = []
for y in range(10):
    row = []
    for x in range(10):
        row.append("+")
    list.insert(0,row)

#print(list)

list[0][0] = "w"
#print(list)

#for row in reversed(list):
#    r = ""
#    for x in row:
#        r += x
#    print(r)

class Position:
    def __init__(self,x,y):
        self.x = x
        self.y = y

pos = Position(5,1)
print(pos.x)

for i in range(20):
    pos = Position(random.randint(0,9),random.randint(0,9))
    while(pos.x == 0 and pos.y == 0):
        pos = Position(random.randint(0,9),random.randint(0,9))
    list[pos.x][pos.y] = "T"

for row in reversed(list):
    r = ""
    for x in row:
        r += x
    print(r)
