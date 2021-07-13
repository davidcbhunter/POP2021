import datetime

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

miura_kentarou = Manga_ka()
miura_kentarou.manga_list.append("Berserk")
miura_kentarou.name = "Miura Kentarou"
miura_kentarou.country = "Japan"
miura_kentarou.publisher = "Young Animal"
miura_kentarou.gender = "Male"
miura_kentarou.date_of_birth = datetime.date(1966,7,11)
miura_kentarou.genre = "Fantasy"
#print(miura_kentarou.manga_list)
print(miura_kentarou)
