a="HELLO"
n=input("Enter number of times that HELLO is needed to be printed:")
try:
    i=0
    while(i<int(n)):
        print (a)
        i+=1
except:
    print("invalid entry")
