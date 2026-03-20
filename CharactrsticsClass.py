import gc

class Demo:
    # Class Variables
    No1 = 10
    No2 = 11
    def __init__(self):
        print("Inside Coustructor")

    def __del__(self):
        print("Inside Destructor")

# class variables need no object
print(Demo.No1)
print(Demo.No2)