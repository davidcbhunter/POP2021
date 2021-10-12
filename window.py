import tkinter as tk

root = tk.Tk()

root.geometry("200x712")

def show_message():
    hello.pack()

hello = tk.Label(root,text = "Hello, world!",cursor = "spider")
#hello.pack()

button = tk.Button(root, text = "Close", command = show_message)

entry = tk.Entry(root, text = "Type", show = "*")

entry.pack()
button.pack()
#hello.pack()

root.mainloop()
