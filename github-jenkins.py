'''
project
1.Display available bikes
2.Request a bike for rent(100rs for 1 bike)
3.Exit
'''
class bikeshop:
    def __init__(self,stock):
        self.stock = stock
    def displayBike(self):
        print("Total Bikes",self.stock)
    def rentforBike(self,q):
        if q<=0:
            print("enter the positive value or greater than zero")
        elif q>self.stock:
            print("enter the value(less than stock)")
        else:
            print("Total Price",q*100)
            print("Total Bikes",self.stock)
obj = bikeshop(100)
while True:
    uc = int(input('''
1.Display Stocks
2.rent a Bike
3.Exit
''' ))
    if uc ==1:
        obj.displayBike()
    elif uc ==2:
        n = int(input("Enter the Qty:---"))
        obj.rentforBike(n)
    else:
        break