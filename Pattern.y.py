n=int(input("enter number"))
i=1
while (i<=n):
        k=1
        while k<=n-i:
                print(" ",end="")
                k=k+1
        star=1
        while (star<=i):
                print("*",end=" ")
                star=star+1
        i=i+2
        print( )
        