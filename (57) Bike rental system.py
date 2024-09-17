class Bike:
    def __init__(self ,stock):
        self.stock=stock
    def displayinfo(self):
        print("Total Bikes ",self.stock)

    def rentforbike(self,q):
        if q<=0:
            print("Enter the real value")
        elif q>self.stock:
            print("Value exceeds the stock available")
        else:
            self.stock=self.stock-q
            print("Total cost",q*100)
            print("Stock left ",self.stock)

while True:
    obj=Bike(100)
    u=int(input('''
                    1 Display stocks
                    2 Rent a bike 
                    3 Exit '''))
    if u==1:
        obj.displayinfo()
    elif u==2:
        n=int(input("Enter the quantity :- "))
        obj.rentforbike(n)
    else:
        break
