def main():
    a=raw_input()
    try:
     if(int(a)>0):
        print(a+" is positive")
     elif(int(a)<0):
        print(a+" is negative")
     else:
        print("the given number is "+a)
    except:
        print("invalid entry")
if __name__ == '__main__':
    main()
