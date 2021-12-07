class Cat:
    def __init__(self,n,g,c,b,a):
        self.name = n
        self.gender = g
        self.color = c
        self.breed = b
        self.age = a
        self.xpos = 0
        self.ypos = 0
        self.energy = 100
    def Jump(self,height):
        #check energy!!
        if self.energy > 5:
            self.Talk()
            #change the ypos
            self.ypos = self.ypos + height
            #make older!
            self.Age()
            #print the ypos
            print(self.ypos)
            #change the ypos back
            self.ypos = self.ypos - height
            #print the ypos again
            print(self.ypos)
        else:
            print("I'm hungry")
    #move function
    def Move(self, distance):
        #check energy!!
        self.xpos = self.xpos + distance
        #make older!
        self.Age()
        print(self.xpos)
    def Age(self):
        self.age = self.age + 0.1
        #lose energy!!
        self.energy = self.energy - 5
    def Talk():
        print("Meow")
    #Get Cat age
    def GetCatAge(self):
        cat_age = self.age * 7
        return cat_age
    #Feed
    def Feed(self):
        self.energy = self.energy + 50



#create a cat
cat = Cat("Tama", "F", "White","Mike", 0)

#age = cat.GetCatAge()
#print(age)
#print(cat.Move(10))

#use while loop to check commands
command = input("\n")
while command != "q":

#give commands to cat using functions

#if command is j, then jump
    if command == "j":
        cat.Jump(10)

#if command is m, then move
    if command == "m":
        d = int(input("How far?\n"))
        cat.Move(d)
#feed the cat
    if command == "f":
        cat.Feed()
    command = input("\n")
















#self.ypos = ypos + height
#print(self.ypos)
#self.ypos = ypos - height
#print(self.ypos)

class CatTwo:
    def __init__(self):
        self.name = ""
        self.gender = ""
        self.color = ""
        self.breed = ""
        self.age = 0

class CatThree:
    def __init__(self,n = "",g = "" ,c = "",b = "",a = 0):
        self.name = n
        self.gender = g
        self.color = c
        self.breed = b
        self.age = a



cat2 = CatTwo()
cat2.name = "Tama"
cat2.gender = "F"
cat2.color = "White"
cat2.breed = "Mike"

cat3 = CatThree("Tama")
#print(cat3.name)



class Dog:
    def __init__(self,n,g,c,b,a):
        self.name = n
        self.gender = g
        self.color = c
        self.breed = b
        self.age = a
