class Cat:
    def __init__(self,n,g,c,b,a):
        self.name = n
        self.gender = g
        self.color = c
        self.breed = b
        self.age = a
        self.xpos = 0
        self.ypos = 0
    def Jump(self,height):
        print("Meow")
        





















self.ypos = ypos + height
        print(self.ypos)
        self.ypos = ypos - height
        print(self.ypos)

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

cat = Cat("Tama", "F", "White","Mike", 0)

cat2 = CatTwo()
cat2.name = "Tama"
cat2.gender = "F"
cat2.color = "White"
cat2.breed = "Mike"

cat3 = CatThree("Tama")
print(cat3.name)



class Dog:
    def __init__(self,n,g,c,b,a):
        self.name = n
        self.gender = g
        self.color = c
        self.breed = b
        self.age = a
