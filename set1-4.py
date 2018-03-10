def main():
    a=raw_input()
    b=raw_input()
    c=raw_input()
    try:
      if(a>b):
        x=a
      else:
        x=b
      if(x>c):
        print(x+" is the largest number")
      else:
        print(c+" is the largest number")
    except:
        print("invalid entry")
if __name__ == '__main__':
    main()
