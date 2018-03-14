n=input("Enter the limit=")
try:
    n=int(n)
    val=int(n*(n+1)/2)
    print(val)
except:
    print("Invalid Entry")
