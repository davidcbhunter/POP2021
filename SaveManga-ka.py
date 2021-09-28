import datetime
import pickle

class Manga_ka:
    def __init__(self):
        self.name = ""
        self.country = ""
        self.publisher = ""
        self.gender = ""
        self.date_of_birth = \
                    datetime.date.today()
        self.manga_list = []
        self.genre = ""
    def __str__(self):
        mangas = "\n"
        for x in self.manga_list:
            mangas += x + "\n"
        return self.name + "\n" + self.publisher \
               + mangas

file = open("Manga-ka List", "rb")

miura_kentarou = pickle.load(file)

file.close()

print(miura_kentarou)
