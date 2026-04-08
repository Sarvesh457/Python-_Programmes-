#Procedural

def CheckEven(No):
    return (No%2 == 0)
        
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