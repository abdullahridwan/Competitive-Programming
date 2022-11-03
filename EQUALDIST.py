t = int(input())
for i in range(0,t):
    a,b = map(int, input().split())
    if ((a+b)%2) == 0:
        print("yes")
    else:
        print("no")