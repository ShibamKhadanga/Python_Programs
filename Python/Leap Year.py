#...........................Find Leap Year

x = int(input("Enter a Year: "))
if (x%4==0):
    if(x%100==0):
        if(x%400==0):
            print(f"{x} is a leap year.")

