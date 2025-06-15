print("do you want a car or a bike?")
print("1. car")
print("2. bike")
choice=int(input("Enter your choice (1 or 2): "))
if choice ==1:
    print("enter 1 for petrol or 2 for diesel")
    x=int(input())
    if x==1:
        print("you have chosen a petrol car")
    else:
        print("you have chosen a diesel car")
else:
    print("you have chosen a bike")