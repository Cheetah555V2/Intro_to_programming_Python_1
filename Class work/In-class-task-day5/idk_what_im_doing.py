#x=float(input());print("B")if(x%2==0 and x%3!=0)else(print("C")if(x%2==0)else(print("D")))

number = float(input())

if (number % 2 == 0 and number % 3 != 0):
    print("B")
elif (number % 2 == 0):
    print("C")
else:
    print("D")