#method constructor
class DemoClass:
    a=10
    def __init__(self):
        print("Welcome to wscubetech")
    def showvalue(self):
        self.c=self.a*self.a
        print(self.c)
    def showvalue1(self):
        print("Welcome to india")
    def showvalue2(self,a,b):
        print(a+b)
obj=DemoClass()
obj.showvalue()
obj.showvalue1()
obj.showvalue2(20,30)
