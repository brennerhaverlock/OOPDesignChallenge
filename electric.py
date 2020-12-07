from auto import Auto
class Electric():

    def __init__(self):
        super().__init__(100000, 4, "Electric", 150)

    balance = 100000
    cars = 0
    #The setWheels and setEngine are also inherited 
    
    def buyCar(self, price):
        """Buy car"""
        if self.balance > price:
            self.balance -= price
            self.cars += 1 
            print("You've bought this car") 
        else:
            print("You don't have enough money to buy this car")


    def sell_car(self, price):
        """Sell car"""
        if self.cars > 1:
            self.balance += price
            self.cars -= 1
        else:
            "You're unable to sell a car due to no cars"

    def start(self):
        print("Car started...Battery on")

    def stop(self):
        print("Engine has been turnedd off")
