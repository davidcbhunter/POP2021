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
    print("OK")

#money = money + customer_money

#print(customer_money)
#print(type(customer_money))
