
# variable argument 

def add(msg,*args):  # * convert all arguments in list
    print(msg)
    sum=0
    for i in range(0,len(args)):
        sum+=args[i]
    return sum 
    
result = add("Hello",1,2,3,4,5,6,7,8,9)
print(result)

"""

Hello
45

"""