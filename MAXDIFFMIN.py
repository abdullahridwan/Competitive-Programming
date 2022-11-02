# cook your dish here
t = int(input())
for i in range(0,t):
    a,b,c = map(int, input().split())
    print(max(a,b,c) - min(a,b,c))