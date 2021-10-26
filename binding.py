import tkinter as tk

root = tk.Tk()
root.geometry("512x512")
root.title("Binding")

#def apress(event):
#    print("a")

def adown(event):
    print("down a")
    label.place_configure(x = label.winfo_x() - 10)

def ddown(event):
    print("down d")
    label.place_configure(x = label.winfo_x() + 10)

#def aup(event):
#    print("up a")

#root.bind('<Key-a>',apress)

root.bind('<KeyPress-a>',adown)
root.bind('<KeyPress-d>',ddown)


#root.bind('<KeyRelease-a>',aup)


im = tk.PhotoImage(file = "person.png")

label = tk.Label(root,image = im)

label.place(x=100,y=100,height = 100, \
            width = 100)





