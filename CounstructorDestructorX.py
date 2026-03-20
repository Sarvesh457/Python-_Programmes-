import gc

class Demo:
    def __init__(self):
        print("Inside Coustructor")

    def __del__(self):
        print("Inside Destructor")

# Allocate
obj1 = Demo()
obj2 = Demo()

# use

del obj1                    # del == free
del obj2

# Deallocate
gc.collect()                # request to gc()

print("End of apptication")