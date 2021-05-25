name = "Super Happy Friendly Vending Machine"

product = "Neru Neru Neru ne"

inventory = 100

money = 20000

cost = 200

def greet_customer():
    print("Welcome to " + name + "\n")

greet_customer()

#customer_money = int(input("Please enter some money \n"))
customer_money = input("Please enter some money \n")

if customer_money.isdigit():
    customer_money = int(customer_money)
    if customer_money >= cost:
        inventory -= 1
        change = customer_money - cost
        money += cost
        print("Your change is " + str(change))
        print("We have " + str(inventory) + product)
        print("Thank you")
    else:
        print("Not enough money")

#money = money + customer_money

#print(customer_money)
#print(type(customer_money))
