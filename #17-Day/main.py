#import Menu
W, M, C, COST = 800, 500, 150, 0.0
class TakingMoney():
    Drinks = {"Latte": {"WATER": 200, "MILK": 150, "COFFEE": 24, "MONEY": 25,},
    "Espresso": {"WATER": 50, "MILK": 0, "COFFEE": 18, "MONEY": 15},
    "Cappuccino": {"WATER": 250, "MILK": 50, "COFFEE": 24, "MONEY": 30}
    }
    def __init__(self, drink):
        self.cup = drink


    def isMoneySufficient(self):
        rup_1 = int(input("How many coins of Rs. 1? "))
        rup_5 = int(input("How many coins of Rs. 5? "))
        rup_10 = int(input("How many coins of Rs. 10? "))
        total_ = eval("rup_1 + 5*rup_5 + 10*rup_10")
        drink_cost = self.Drinks[self.cup]["MONEY"]
        if drink_cost > total_:
            print(f"You did not enter sufficient money, You need Rs. {drink_cost - total_} more.")
            return False, False
        return (True, total_ - drink_cost)



    def isResourceSufficient(self):
        w, m, c, cost = self.Drinks[self.cup].values()
        if W<w:
            print("Sorry not enough water.")
        elif M<m:
            print("Sorry not enough mil.")
        elif C<c:
            print("Sorry not enough coffee.")
        elif (W>=w) and (M>=m) and (C>=c):
            return True
        return False

    def updateResource(self):
        w, m, c, cost = self.Drinks[self.cup].values()
        global W, M, C, COST
        W -= w
        M -= m
        C -= c
        COST += cost
        #print(W, M, C, COST)

#ob_  =  TakingMoney("Latte")

#ob_.Resource = {"WATER": 300, "MILK": 200, "COFFEE": 100, "MONEY": 0.0}

while True:
    print("----------------------------")
    print("What would you like to have \n☕Latte: ₹25 \n☕Espresso: ₹15 \n☕Cappuccino: ₹30\n----------------------------")
    drink = input()
    if drink in ['Latte', 'Espresso', 'Cappuccino']:
        ob = TakingMoney(drink)
        cond, sum_ = ob.isMoneySufficient()
        if cond:
            if ob.isResourceSufficient():
                ob.updateResource()
                if sum_ > 0:
                    change = f'\nPlease don\'t forget your Rs.{sum_}'
                else:
                    change = ""
                print(f"\nEnjoy your {drink}☕ {change}")
    elif drink == 'report':
        repo = f"Water: {W}\nmilk:{M}\ncoffe: {C}\nmoney: {COST}"
        report_ = f'''
+------------+-----------+
| Water      |{W}  {" " * (9 - len(str(W)))}|
+------------+-----------+
| Milk       |{M}  {" " * (9 - len(str(M)))}|
+------------+-----------+
| Coffee     |{C}  {" " * (9 - len(str(C)))}|
+------------+-----------+
| Money      |{COST}  {" " * (9 - len(str(COST)))}|
+------------+-----------+
             '''
        print(report_)
    else:
        print("Please choose correct option.")

