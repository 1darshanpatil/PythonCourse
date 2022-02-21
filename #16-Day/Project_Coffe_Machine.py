WATER = 300
MILK = 200
COFFEE = 100
MONEY = 0.0



def updateResource(drink_):
    Latte = {"Water": 200, "Milk": 150, "Coffee": 24, "Price": 25}
    Espresso = {"Water": 50, "Milk": 0, "Coffee": 18, "Price": 15}
    Cappuccino = {"Water": 250, "Milk": 50, "Coffee": 24, "Price": 30}
    cup = {"Latte": Latte, "Espresso": Espresso, "Cappuccino": Cappuccino}
    global WATER, MILK, COFFEE, MONEY
    if WATER < cup[drink_]['Water']:
        print("Not enough water.")
    if MILK < cup[drink_]['Milk']:
        print("NOt enough milk.")
    if COFFEE < cup[drink_]['Coffee']:
        print("Not enough coffee.")
    if (WATER >= cup[drink_]['Water']) and (MILK >= cup[drink_]['Milk']) and (COFFEE >= cup[drink_]['Coffee']):
        WATER -= cup[drink_]['Water']
        MILK -= cup[drink_]['Milk']
        COFFEE -= cup[drink_]['Coffee']
        MONEY += cup[drink_]['Price']
        return True
    return False



def takingMoney(drink_):
    rup_1 = int(input("How many coins of 1₹? "))
    rup_5 = int(input("How many coins of 5₹? "))
    rup_10 = int(input("How many coins of 10₹ "))
    total_ = eval("rup_1 + 5*rup_5 + 10*rup_10")
    price = 30
    if drink_ == "Latte":
        price = 25
    if drink_ == "Espresso":
        price = 15
    if price > total_:
        print(f"Not enough to buy {drink_}, you need ₹{price - total_} more\n Your sum of ₹{total_} has been refunded.")
        return False
    if updateResource(drink_):
        print(f"Enjoy Your {drink}☕!")
        print(f"Don't forget to take your change ₹{total_ - price}")




while True:
    print("----------------------------")
    print("What would you like to have \n☕Latte: ₹25 \n☕Espresso: ₹15 \n☕Cappuccino: ₹30\n----------------------------")
    drink = input()
    if drink in ['Latte', 'Espresso', 'Cappuccino']:
        takingMoney(drink)
    elif drink == 'report':
        repo = f"Water: {WATER}\nmilk:{MILK}\ncoffe: {COFFEE}\nmoney: {MONEY}"
        report_ = f'''
        +------------+-----------+
        | Water      |{WATER}  {" "*(9 - len(str(WATER)))}|
        +------------+-----------+
        | Milk       |{MILK}  {" "*(9 - len(str(MILK)))}|
        +------------+-----------+
        | Coffee     |{COFFEE}  {" "*(9 - len(str(COFFEE)))}|
        +------------+-----------+
        | Money      |{MONEY}  {" "*(9 - len(str(MONEY)))}|
        +------------+-----------+
        '''
        print(report_)
    else:
        print("Please choose correct option.")

