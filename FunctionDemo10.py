# One Function can call another function

def fun():
    print("Inside fun")
    
def gun():
    print("Inside gun")
    fun()                           # call for another function from a function    main->gun->fun

def main():
    gun()

if __name__ == "__main__":
    main()
