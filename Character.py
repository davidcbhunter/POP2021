import pickle
import os

class Character:
    def __init__(self, n = "", h = 1):
        self.name = n
        self.hp = h

data = Character()

if os.path.exists("character"):
    file = open("character","rb")
    data = pickle.load(file)
    file.close()
else:
    file = open("character","wb")
    data.name = "David"
    data.hp = 100
    pickle.dump(data,file)
    file.close()

print(data.name)
print(data.hp)

    
