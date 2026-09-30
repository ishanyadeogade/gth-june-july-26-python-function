
def fact(num):
    f=1
    while num>1:
        f*=num
        num-=1
    return f
    
num = int(input("Enter a number: "))

print("Factorial of",num,"is:",fact(num))

"""

Enter a number: 5
Factorial of 5 is: 120

"""
        