N=int(input())
for i in range(N):
    X=int(input())
    c=0
    for j in range(1,X):
        if(X%j==0):
            c=c+1
            print(j)
            if (c>2):
                print(X,"nao eh primo")
            else:
                print(X,"eh primo")
