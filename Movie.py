class Movie:
    def __init__(self, ti,di,ca,ge,rt):
        self.title = ti
        self.director = di
        self.cast = ca
        self.genre = ge
        self.runtime = rt

dca = ["Timothee Chalime","Oscar Isaac","Jessica Duncan","Zandaya"]
movie = Movie("Dune","Denis Villenvue",dca,"SF",146)

lotrca = ["Sean Astin","Vigo Mortenson","Ian McKellan","Sean Bean"] 
movie2 = Movie("The Lord of the Rings","Peter Jackson", lotrca, "Fantasy", 540)


print(movie2.cast)
