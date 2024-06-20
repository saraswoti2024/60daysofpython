###=============================================coffee making machine project==============================================
import menu
from menu import MENU


def sufficient_Resource(ordered):
    for item in ordered:
        if(ordered[item]>resources[item]):
            print(f"sorry there is not enough {item}")
            return False
        else:
            return True

def process_coins():
    total = int(input("quarter coins: "))*0.25
    total += int(input("dimes coins: "))*0.10
    total += int(input("nickles coins: "))*0.05
    total += int(input("pennies coins: "))*0.01
    return total

def is_transaction(payment_cost,drink_cost):

    if(payment_cost>=drink_cost):
        change = round((payment_cost-drink_cost),2)
        print(f"here is ${change} in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("sorry thats not enough money.Money refundend.")
        return False



def make_coffee(choices,ingredients):
    for i in ingredients:
        resources[i] -=ingredients[i]
    print(f"here's your {choice} coffee")



print("COFFEE MACHINE")
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

on = True
profit=0
while(on):
    print("--------------------------------------------")
    print("Availabe resource")
    print(f"Water : {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"coffee : {resources['coffee']}gm")
    print(f"Money : ${profit}")
    choice = input("choose a drink(latte/cappuccino/espresso): ").lower()
      
    
    if choice=="off":
        on = False

    else:
        drink = MENU[choice]
        if sufficient_Resource(drink["ingredients"]):
            payment = process_coins()           
            if is_transaction(payment,drink["cost"]):
                make_coffee(choice,drink["ingredients"])
