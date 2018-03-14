n=input("Enter the limit=")
try:
    n=int(n)
    sum=int(n*(n+1)/2)
    print(sum)
except:
    print("Invalid Entry")
