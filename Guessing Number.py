i=1
k=11
while (i<=5):
    n=int(input("enter number"))
    if (n>k):
        print("High Guessing")
    elif (n<k):
        print("Low Guessing")
    elif (n==k):
        print("You are Win")
        break
    else:
        print("You are loose")
    i=i+1
    print()
    
    