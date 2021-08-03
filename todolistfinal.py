import datetime
import os
import pickle

class ToDoItem:
    def __init__(self,td,dd):
        self.todo = td
        self.due_date = dd
        self.finished = False
    def __repr__(self):
        st = ""
        if self.finished:
            st += "☑"
        else:
            st += "☐"
        st += " " + self.todo + " (" + str(self.due_date) + " )"
        return st



class ToDoList:
    def __init__(self):
        self.tdl = []
    def Add(self,td):
        self.tdl.append(td)
    def Remove(self,index):
        self.tdl.removeat(index)
    def MarkFinished(self,index):
        self.tdl[index].finished = True
    def ShowItems(self):
        for item in self.tdl:
            print( str(self.tdl.index(item) + 1) + " " + str(item))
    def Save(self):
        file = open("todolist", "wb")
        pickle.dump(self,file)
        file.close()


todo1 = ToDoItem("Do HW",datetime.date.today())
print(todo1.todo)
print(todo1.due_date)
print(todo1.finished)

#tdl1 = ToDoList()
#tdl1.tdl.append(todo1)

def ShowChoices():
    print("1 Add Item")
    print("2 Remove Item")
    print("3 Finish Item")
    print("Q Quit")
    print("Enter a number (1,2,3) or Q to quit")

#file = open("todolist", "wb")
#file.close()

tdl1 = ToDoList()

if os.path.exists("todolist"):
    file = open("todolist", "rb")
    if os.stat("todolist").st_size != 0:
        tdl1 = pickle.load(file)
    file.close()



print(tdl1.tdl)

ShowChoices()
userchoice = input("What would you like to do? \n")
while userchoice.lower() != "q":
    if userchoice.isdigit():
        if int(userchoice) == 1:
            #print("adding \n")
            tdn = input("Enter the todo item \n")
            tdd = datetime.datetime.strptime(input("Enter the due date (YYYY-MM-DD) \n"),"%Y-%m-%d")
            tdl1.Add(ToDoItem(tdn,tdd))
            tdl1.Save()
            #print(tdl1.tdl)
        elif int(userchoice) == 2:
            #print("removing \n")
            tdl1.ShowItems()
            index = int(input("Select an item")) - 1
            tdl1.Remove(index)
            tdl1.Save()
        elif int(userchoice) == 3:
            #print("finishing \n")
            tdl1.ShowItems()
            index = int(input("Select an item")) - 1
            tdl1.MarkFinished(index)
            tdl1.Save()
        else:
            print("Sorry. I don't understand. \n")
    else:
        print("Sorry. I don't understand. \n")
    ShowChoices()
    userchoice = input("What would you like to do? \n")


