import tkinter as tk

root = tk.Tk()

root.title("Listbox")
root.geometry("512x512")

#dca = tk.StringVar()
#dca.set("Timothee_Chalime Oscar_Isaac Jessica_Duncan Zandaya")

#lb = tk.Listbox(root, listvariable = dca)
#lb.pack()

#cb = tk.Checkbutton(root)
#cb.pack()

btnText = tk.StringVar()
btnText.set("Hello")

x = 1
def change():
    global x
    btnText.set("Hello" + str(x))
    x +=1

button = tk.Button(root,command = change)
label = tk.Label(root, textvariable = btnText)
button.pack()
label.pack()





root.mainloop()
