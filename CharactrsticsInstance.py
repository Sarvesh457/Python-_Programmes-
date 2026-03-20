import gc

class Demo:
    # Class Variables               Global
    No1 = 10
    No2 = 11
    def __init__(self):
        # Instance Variables            Local
        self.A = 101
        self.B = 201
        print("Inside Coustructor")

    def __del__(self):
        print("Inside Destructor")

# class variables need no object
print(Demo.No1)
print(Demo.No2)

obj = Demo()
# Instance Variables needs object to access
print(obj.A)
print(obj.B)