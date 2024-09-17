class Area:
    def find_area(self,x=None,y=None):
        if x!=None and y!=None:
            print(x*y)
        elif x!=None:
            print(x*x)
        else:print('Nothing found')
obj=Area()
obj.find_area()
obj.find_area(10)
obj.find_area(10,20)


#Method overriding
class Area:
    def findarea(self):
        print("area is A")
class Volume(Area):
    def findarea(self):
        print("Volume is B")

obj=Volume()
obj.findarea()
