class A:
    def displayA(self):
        print('welcome to wscubetech A')
class B:
    def displayB(self):
        print('welcome to wscubetech B')

class C(A,B):
    def displayC(self):
        print('welcome to wscubetech C')


obj=C()
obj.displayA()
obj.displayB()     #MULTIPLE INHERITANCE IS ONLY SUPPORTED IN PYTHON
obj.displayC()
