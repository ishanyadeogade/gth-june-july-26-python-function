
def table(n,count=1):
    
    if count<=10:
        print(n*count)
        count+=1
        table(n,count)
        
num = int(input("Enter a number : ")) 
table(num)

"""

Enter a number : 5
5
10
15
20
25
30
35
40
45
50

"""
