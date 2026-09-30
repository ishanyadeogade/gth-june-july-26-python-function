
def cal_per(marks_list):
    sum=0
    for i in range(0,len(marks_list)):
        sum+=marks_list[i]
    
    return sum/len(marks_list)
    
    
    
sub_count= int(input("Enter the subject count : "))
marks_list=[0]*sub_count

for i in range (0,sub_count):
    marks_list[i]=int(input("Enter the marks for subject "+str((i+1))+": "))
    
print("Percentage : ",cal_per(marks_list))


"""

Enter the subject count : 6
Enter the marks for subject 1: 45
Enter the marks for subject 2: 50
Enter the marks for subject 3: 60
Enter the marks for subject 4: 75
Enter the marks for subject 5: 95
Enter the marks for subject 6: 90
Percentage :  69.16666666666667


"""