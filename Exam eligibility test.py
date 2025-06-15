x=int(input("Enter your attendance:: "))
l=input("Do you have a medical condition? y/n:: ")
if l=="y":
    print("You are allowed to attend the test.")
else:
    if x>75:
        print(" You are allowed to attend the test.")

    else:
        print("You are not allowed to attend the test.")
