class Ingredient:
    def __init__(self,a,u,t):
        self.amount = a
        self.unit = u
        self.thing = t
    def __str__(self):
        return str(self.amount) + "\t" + self.unit \
               + "\t" + self.thing
    def __repr__(self):
        return str(self.amount) + "\t" + self.unit \
               + "\t" + self.thing

#flour = Ingredient(1.75,"cup","all-purpose flour")
#print(flour)

class Recipe:
    def __init__(self,i, d):
        self.ingredients = i
        self.directions = d
    def print_recipe(self):
        for ingredient in self.ingredients:
            print(ingredient)
        for dir in range(len(self.directions)):
            print(str(dir + 1) + ". " + self.directions[dir])

ing = [Ingredient(50,"ml","sugar"),Ingredient(50,"ml","water")]

dir = []
dir.append("Put the sugar and water in a pot.")
dir.append("Mix and heat until it changes to a caramel color.")
dir.append("Pour it onto wax paper laid on a baking sheet.")
dir.append("Stick a toothpick in it and let it cool.")

bekko_ame = Recipe(ing,dir)

bekko_ame.print_recipe()
#dir.append("これは日本語")
#print(dir[1])
