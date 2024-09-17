l=[10,20,30,40]
print(len(l))
s="welcome"
print(len(s))

class Wscubettech:
    def displayinfo(self,name=""):
        print("Welcome to wscubtech"+name)
obj=Wscubettech()
obj.displayinfo()
obj.displayinfo('Python')

class IIT(Wscubettech):
    def displayinfo(self):
        super().displayinfo()
        print("Welcome to IIT")

obj=IIT()
obj.displayinfo()
