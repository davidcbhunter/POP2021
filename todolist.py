import datetime

class ToDoItem:
    def __init__(self,td,dd):
        self.todo = td
        self.due_date = dd
        self.finished = False

todo1 = ToDoItem("Do HW",datetime.date.today())
print(todo1.todo)
print(todo1.due_date)
print(todo1.finished)

class ToDoList:
    def __init__(self):
        self.tdl = []
    def Add(self,td):
        self.tdl.append(td)
    def Remove(self,index):
        self.tdl.removeat(index)

tdl1 = ToDoList()
tdl1.tdl.append(todo1)
