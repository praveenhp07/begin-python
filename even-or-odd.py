def main():
    a=input()
    try:
     x=int(a)%2
     if(int(x)==0):
        print("even")
     else:
        print("odd")
    except:
        print("invalid entry")
if __name__ == '__main__':
    main()
