N=int(input())
for i in range(N):
    A=int(input())
    if A<0 and A%2==0:
        print("EVEN NEGATIVE")
    elif A>0 and A%2==0:
        print("EVEN POSITIVE")
    elif A<0 and A%2==1:
        print("ODD NEGATIVE")
    elif A>0 and A%2==1:
        print("ODD POSITIVE")
    else:
        print("NULL")