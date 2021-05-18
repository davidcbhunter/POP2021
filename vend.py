name = "Super Happy Friendly Vending Machine"

product = "Neru Neru Neru ne"

inventory = 100

money = 20000

cost = 200

def greet_customer():
    print("Welcome to " + name + "\n")

greet_customer()

#customer_money = input()

#print(customer_money)
#print(type(customer_money))

#customer_money = int(customer_money)

#if customer_money >= cost:
    #
    #inventory -= 1
    #change = (customer_money - cost)
    #money = money - change
    #print("Here is your change " + str(change))
    #print("Thank you!")
    #print(money)
    #print(inventory)
#else:
    #customer_money = input()

    #print(customer_money)
    #print(type(customer_money))

    #customer_money = int(customer_money)

customer_money = input()
customer_money = int(customer_money)

def recheck_money():
    global customer_money
    customer_money = input()
    customer_money = int(customer_money)


while(customer_money < cost):
    recheck_money()

inventory -= 1
change = (customer_money - cost)
money = money - change
print("Here is your change " + str(change))
print("Thank you!")
print(money)
print(inventory)
