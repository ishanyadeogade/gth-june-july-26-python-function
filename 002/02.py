
def pow(base,index):
    p=1
    while index>0:
        p*=base
        index-=1
    
    print("Result :",p)
    

base = int(input("Enter the base : "))
index = int(input("Enter the index : "))

pow(base,index)   # function call

"""

Enter the base : 4
Enter the index : 3
Result : 64

"""