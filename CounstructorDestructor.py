import gc

class Demo:
    def __init__(self):
        print("Inside Coustructor")

    def __del__(self):
        print("Inside Destructor")

# Allocate
obj = Demo()

# use

del obj                     # del == free

# Deallocate
gc.collect()                # request to gc()

print("End of apptication")