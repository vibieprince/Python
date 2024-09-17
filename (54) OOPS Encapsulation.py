#Getter and setter
class Student:
    def __int__(self):
        self.__name=""
    def getname(self):
        return
    def setname(self,name):
        self.__name=name
obj=Student()
obj.setname("Testing")
name=obj.getname()
print(name)


class Student:
    __name="Prince"
    def __init__(self):
        print(self.__name)
    def __displayinfo(self):
        print("Welcome to Inida")

obj=Student()
