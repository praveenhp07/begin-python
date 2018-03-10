def main():
    a=raw_input()
    try:
     x=['a','e','i','o','u','A','E','I','O','U']
     if(str(a) in x):
        print(a+" is vowel")
     else:
        print(a+" is not vowel")
    except:
        print("invalid entry")
if __name__ == '__main__':
    main()
