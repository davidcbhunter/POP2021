import random

class Character:
    def __init__(self,n,g):
        self.name = n
        self.greeting = g #あいさつ

    def greet(self):
        print(self.greeting + ", I'm " + self.name)


gList = ["Hey","Hello","Hi!","Yo!","What's up?","Que pasa", "How do you do?"] #あいさつリスト

nList = ["Tomoko","James","Claire","Susan","Bill","Yuri","Mary"] #名前リスト

cList = [] #your character list

#add 7 characters to cList - we need a name and a greeting
#to add something to a list, use list.append(x)
for x in nList:
    c = Character(x,gList[random.randint(0,len(gList)-1)])
    cList.append(c)

print(cList[0].name)
print(cList[0].greeting)

#have the characters do a greeting (あいさつする)
for x in cList:
    x.greet()







