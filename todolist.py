import datetime

class ToDoItem:
    def __init__(self,td,dd):
        self.todo = td
        self.due_date = dd
        self.finished = False

#todo1 = ToDoItem("Do HW",datetime.date.today())
#print(todo1.todo)
#print(todo1.due_date)
#print(todo1.finished)

class ToDoList:
    def __init__(self):
        self.tdl = []
    def Add(self,td):
        self.tdl.append(td)
    def Remove(self,index):
        self.tdl.pop(index)
    def ShowList(self):
        for x in self.tdl:
            print(x.todo + " " + str(x.due_date) + " " + str(x.finished) )

tdl1 = ToDoList()
#tdl1.tdl.append(todo1)



def ShowCommand():
    print("Q for quit")
    print("A for add")
    print("R for remove")
    print("f for finish")
    print("\n")
    
ShowCommand()
command = input("Please enter your command \n")

while command != "Q":
    if command == "A":
        todo_name = input("Please enter your todo item \n")
        todo_year = int(input("Please enter the year \n"))
        todo_month = int(input("Please enter the month \n"))
        todo_day = int(input("Please enter the day \n"))
        todo2 = ToDoItem(todo_name,datetime.date(todo_year,todo_month,todo_day))
        tdl1.Add(todo2)
        tdl1.ShowList()
    if command == "R":
        tdl1.ShowList()
        to_remove = int(input("Enter the number for the item"))
        if to_remove <= 0:
            print("Your number is too small.")
        if to_remove > len(tdl1.tdl):
            print("Your number is too big.")
        tdl1.Remove(to_remove-1)
    command = input("Please enter your command \n")
