# cook your dish here
t=int(input())
for i in range(t):
    n, x= map(int, input().split())
    
    to_buy=n-x
    
    a=(n-x)/4
    if n>x:
        if (n-x)%4==0:
            print(int(a))
        else:
            print(int(a)+1)
    else:
        print("0")
    