class Parent:
    def __init__(self):
        print("Inside parent constructor")
        self.No1 = 10
    
    def fun(self):
        print("Inside fun method of parent")                               #

class Child(Parent):
    def __init__(self):
        super().__init__()                                                 # if instance it need the super call
        print("Inside Child constructor")
    
    def fun(self):
        super().fun()                                                       # print of parent class                                                    
        print("Inside fun method of child")

cobj = Child()

cobj.fun()
