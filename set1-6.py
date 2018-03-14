def main():
    year=input("Enter year to be checked:")
    try:

        if(int(year)%4==0 and int(year)%100!=0 or int(year)%400==0):
            print("This year is a leap year!")
        else:
            print("This year is not a leap year!")
    except:
        print("Invalid entry")
if __name__ == '__main__':
    main()
