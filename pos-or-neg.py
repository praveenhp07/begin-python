 a=input()
    try:
     if(int(a)>0):
        print("positive")
     elif(int(a)<0):
        print("negative")
     else:
        print("the given number is "+a)
    except:
        print("invalid entry")
