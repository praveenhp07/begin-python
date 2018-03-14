try:
    n=int(input("enter no. of terms"))
    i=0
    a=[int(input()) for i in range(0,n)]
    b=int(input("Enter no of terms to be added:"))
    i=0
    s=0
    while(i<b):
        s=int(s)+a[i]
        i=i+1
    print("sum of integers is:"+str(s))
except:
    print("Invalid Entry")
