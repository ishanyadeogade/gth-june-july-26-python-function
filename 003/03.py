
def get_power(base,index,res=1):
    if index>0:
        res*=base 
        index-=1
        get_power(base,index,res)
    else :
        print(res)

base = int(input("Enter a base : "))
index = int(input("Enter a index : "))

get_power(base,index) # (2,4) --> 2*2, 4*2, 8*2, 16*2

""" 

Enter a base : 2
Enter a index : 4
16

"""