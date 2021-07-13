class Ingredient:
    def __init__(self,a,u,t):
        self.amount = a
        self.unit = u
        self.thing = t
    def __str__(self):
        return str(self.amount) + "\t" + self.unit \
               + "\t" + self.thing

#flour = Ingredient(1.75,"cup","all-purpose flour")
#print(flour)

class Recipe:
    def __init__(self,i, d):
        self.ingredients = i
        self.directions = d

ing = [Ingredient(50,"ml","sugar"),Ingredient(50,"ml","water")]
print(ing)
