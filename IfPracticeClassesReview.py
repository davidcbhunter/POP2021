# if practice
import math


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

pos = Position(5,5)


pos2 = Position(9,9)

print(id(pos))
print(id(pos2))
#t = pos
#print(t.x)
#print(t.y)

# compare pos and pos2
if pos.Distance(pos2) > 5:
    print("far")
else:
    print("close")

pos3 = Position(0,1)

pos4 = Position(2,2)


#compare distance between pos & pos2 and pos3 & 4
if pos.Distance(pos2) > pos3.Distance(pos4):
    print("bigger")
else:
    print("smaller")






# classes review

class Job:
    def __init__(self,n,s):
        self.name = n
        self.salary = s
    def Promotion(self,n,d):
        self.name = n
        self.salary += d

# make job
job = Job("CEO",10000000000)

print(job.name)
print(job.salary)

# get promotion


print(job.name)
print(job.salary)








