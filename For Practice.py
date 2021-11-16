import random

class Character:
    def __init__(self,n,g):
        self.name = n
        self.greeting = g #あいさつ

    def greet(self):
        print(self.greeting + ", I'm " + self.name)


gList = ["Hey","Hello","Hi!","Yo!","What's up?","Que pasa", "How do you do?"]

nList = ["Tomoko","James","Claire","Susan","Bill","Yuri","Mary"]

cList = []

#add 7 characters to cList - we need a name and a greeting
#to add something to a list, use list.append(x)


#have the characters do a greeting (あいさつする)
