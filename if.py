import datetime
fruit = input("What is your favorite fruit? \n")
fruits = ["apple","orange","banana",\
          "pineapple","grape","grapefruit"]

#print(type(fruits))
#print(type(fruits[0]))
#print(type(fruits[-1]))

#length
#print(len(fruits))

if fruit in fruits:
    #print("I know that fruit!!")
    print("I like " + fruit + "s, too.")
else:
    print("I don't know that fruit!")
    fruits.append(fruit)
    print(fruits)

#if fruit == "apple":
#    print("I like apples, too")
#elif fruit == "orange":
#    print("I like oranges, too")
#elif fruit == "pineapple":
#    print("I like pineapples, too")
#else:
#    print("I don't know that fruit")

#if fruit == "apple":
#    print("I like apples, too")
#else:
#    if fruit == "orange":
#        print("I like oranges, too")
#    else:
#        if fruit == "pineapple":
#            print("I like pineapples, too")
#        else:
#            print("I don't know that fruit")
