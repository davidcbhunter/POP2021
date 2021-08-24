import datetime
import os
import pickle
import tkinter as tk
from tkinter import font

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
        if len(self.tdl) > 0:
            found = False
            for item in self.tdl:
                if item.finished:
                    self.tdl.insert(self.tdl.index(item),td)
                    found = True
                    break
            if not found:
                self.tdl.append(td)
        else:
            self.tdl.append(td)
    def Remove(self,index):
        self.tdl.pop(index)
    def MarkFinished(self,index):
        self.tdl[index].finished = True
        self.tdl.append(self.tdl.pop(index))
    def MarkUnfinished(self,index):
        self.tdl[index].finished = False
    def ShowItems(self):
        for item in self.tdl:
            print( str(self.tdl.index(item) + 1) + " " + str(item))
    def Save(self):
        print("Saving")
        file = open("todolist", "wb")
        pickle.dump(self,file)
        file.close()



#todo1 = ToDoItem("Do HW",datetime.date.today())
#print(todo1.todo)
#print(todo1.due_date)
#print(todo1.finished)

#tdl1 = ToDoList()
#tdl1.tdl.append(todo1)

#def ShowChoices():
#    print("1 Add Item")
#    print("2 Remove Item")
#    print("3 Finish Item")
#    print("Q Quit")
#    print("Enter a number (1,2,3) or Q to quit")

#file = open("todolist", "wb")
#file.close()

tdl1 = ToDoList()

if os.path.exists("todolist"):
    file = open("todolist", "rb")
    if os.stat("todolist").st_size != 0:
        tdl1 = pickle.load(file)
    file.close()

def setV(index,val):
    if val.get():
        tdl1.MarkFinished(index)
    else:
        tdl1.MarkUnfinished(index)
        
    #print("here")
#    for v in values:
#        if v.get():
#            tdl1.MarkFinished(values.index(v))
#        else:
#            tdl1.MarkUnfinished(values.index(v))
    tdl1.Save()

def setTodo():
    print("here")
    for v in todos:
        print(todos.index(v))
        print(len(tdl1.tdl))
        print(len(todos))
        tdl1.tdl[(todos.index(v))].todo = v.get()
    tdl1.Save()

root = tk.Tk()
root.geometry("700x600")

font = font.Font(family = "Helvetica",size = 24)

x = 0

def Close():
    setTodo()
    root.destroy()

def Del(index):
    print(index)
    tdl1.Remove(index)
    rows[6*index].destroy()
    rows[(6*index)+1].destroy()
    rows[(6*index)+2].destroy()
    rows[(6*index)+3].destroy()
    rows[(6*index)+4].destroy()
    rows[(6*index)+5].destroy()
    rows.pop(6*index)
    rows.pop((6*index))
    rows.pop((6*index))
    rows.pop((6*index))
    rows.pop((6*index))
    rows.pop((6*index))
    
    values.pop(index)
    todos.pop(index)
    years.pop(index)
    months.pop(index)
    days.pop(index)
    
    tdl1.Save()

def Add():
    global x
    todo = ToDoItem("",datetime.date.today())
    tdl1.Add(todo)
    tdl1.Save()
    print(len(tdl1.tdl))
    val = tk.BooleanVar()
    ##val.set(todo.finished)
    ##print(todo.finished)
    check = tk.Checkbutton(root, variable = val,command = lambda: setV(tdl1.tdl.index(todo),val))
    #if todo.finished:
    #    check.select()
    #else:
    #    check.deselect()
    check.grid(column = 0, row = x)
    rows.append(check)

    values.append(val)
    en = tk.StringVar()
    en.set("")
    todos.append(en)
    entry = tk.Entry(root, font = font,textvariable = en)
    entry.grid(column = 1, row =x)
    rows.append(entry)

    year = tk.StringVar()
    year.set(str(todo.due_date.year))
    years.append(en)
    entry = tk.Entry(root, font = font,textvariable = year)
    entry.grid(column = 2, row =x)
    rows.append(entry)

    month = tk.StringVar()
    month.set(str(todo.due_date.month))
    months.append(en)
    entry = tk.Entry(root, font = font,textvariable = month)
    entry.grid(column = 3, row =x)
    rows.append(entry)

    day = tk.StringVar()
    day.set(str(todo.due_date.day))
    days.append(en)
    entry = tk.Entry(root, font = font,textvariable = day)
    entry.grid(column = 4, row =x)
    rows.append(entry)
    
    delButton = tk.Button(root,text= "Delete", command = lambda: Del(tdl1.tdl.index(todo)))
    delButton.grid(column = 5, row = x)
    rows.append(delButton)
    #print(len(rows))
    x += 1
    addButton.grid(row = x)
    button.grid(row = x+1)


values = []
todos = []
years = []
months = []
days = []
rows = []
for todo in tdl1.tdl:
    val = tk.BooleanVar()
    val.set(todo.finished)
    print(todo.finished)
    check = tk.Checkbutton(root, variable = val,command = setV)
    rows.append(check)
    #if todo.finished:
    #    check.select()
    #else:
    #    check.deselect()
    check.grid(column = 0, row = x)
    values.append(val)
    en = tk.StringVar()
    en.set(todo.todo)
    todos.append(en)
    entry = tk.Entry(root,font = font, textvariable = en)
    entry.grid(column = 1, row =x)
    rows.append(entry)

    year = tk.StringVar()
    year.set(str(todo.due_date.year))
    years.append(en)
    entry = tk.Entry(root,font = font, textvariable = year)
    entry.grid(column = 2, row =x)
    rows.append(entry)

    month = tk.StringVar()
    month.set(str(todo.due_date.month))
    months.append(en)
    entry = tk.Entry(root,font = font, textvariable = month)
    entry.grid(column = 3, row =x)
    rows.append(entry)

    day = tk.StringVar()
    day.set(str(todo.due_date.day))
    days.append(en)
    entry = tk.Entry(root,font = font, textvariable = day)
    entry.grid(column = 4, row =x)
    rows.append(entry)

    delButton = tk.Button(root,text= "Delete", command = lambda: Del(tdl1.tdl.index(todo)))
    delButton.grid(column = 5, row = x)
    rows.append(delButton)
    print(len(rows))
    x += 1

addButton = tk.Button(root,text= "Add Todo item", command = Add)
addButton.grid(column = 2)

button = tk.Button(root,text= "Close the window", command = Close)

button.grid(column = 2)

root.mainloop()
