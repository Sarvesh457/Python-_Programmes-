#Procedural

def CheckEven(No):
    if (No%2 == 0):
        return True
    else:
        return False
        
def main():
    Value = 0
    Ret = False
    
    print("Enter the Number : ")
    Value = int(input())
    
    Ret = CheckEven(Value)
    
    if(Ret == True) :
        print("The Number is Even")
    else :
        print("The Number is Odd")

if __name__ == "__main__":
    main()