# cook your dish here
t = int(input())
for i in range(0, t):
    x, y = map(int, input().split())
    if 2*x > 5*y:
        print("Chocolate")
    elif 2*x < 5*y:
        print("Candy")
    else:
        print("Either")