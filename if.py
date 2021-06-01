fruit = input("What is your favorite fruit? \n")

if fruit == "apple":
    print("I like apples, too")
elif fruit == "orange":
    print("I like oranges, too")
elif fruit == "pineapple":
    print("I like pineapples, too")
else:
    print("I don't know that fruit")

if fruit == "apple":
    print("I like apples, too")
else:
    if fruit == "orange":
        print("I like oranges, too")
    else:
        if fruit == "pineapple":
            print("I like pineapples, too")
        else:
            print("I don't know that fruit")
