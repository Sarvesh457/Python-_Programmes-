No = 11                                         # Global

def Fun():
    global No                                   # Reference to global
    print("Value of no from fun is : ",No)      # 11
    No = No + 1
    print("Value of no from fun is : ",No)      # 12 

print("Value of No is : ",No)                   # 11
Fun()
print("Value of No is : ",No)                   # 12