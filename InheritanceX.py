class Parent:
    def __init__(self):
        print("Inside parent constructor")
        self.No1 = 10
        self.No2 = 20
    
    def fun(self):
        print("Inside fun method of parent",self.No1,self.No2)

class Child(Parent):
    def __init__(self):
        super().__init__()                                                 # if instance it need the super call
        print("Inside Child constructor")
        self.A = 11
        self.B = 21
    
    def sun(self):
        print("Inside sun method of child",self.A,self.B,self.No1,self.No2)   # can access parent members

cobj = Child()

# A child class can directly call the parent class Data members
print(cobj.No1) # 10
print(cobj.No2) # 20

print(cobj.A)   # 11
print(cobj.B)   # 21

# A child class can directly access the parent class Data method
cobj.fun()

cobj.sun()