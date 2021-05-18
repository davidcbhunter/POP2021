name = "Super Happy Friendly Vending Machine"

product = "Neru Neru Neru ne"

inventory = 100

money = 20000

cost = 200

def greet_customer():
    print("Welcome to " + name + "\n")

greet_customer()

customer_money = input()

print(customer_money)
print(type(customer_money))
