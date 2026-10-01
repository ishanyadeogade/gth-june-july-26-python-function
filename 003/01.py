
def show(x):
    if x==0:  # base condition
        print("stop")
    else :
        print("Hello, Python")
        x-=1
        show(x) # recursive call
        
        
show(5);

"""

Hello, Python
Hello, Python
Hello, Python
Hello, Python
Hello, Python
stop

"""
