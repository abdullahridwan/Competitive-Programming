T = int(input())
for i in range(0, T):
    a,b,c = map(int, input().split())
    bids = [a, b, c]
    idx = bids.index(max(bids))

    if idx == 0:
        print("Alice")
    elif idx == 1:
        print("Bob")
    else:
        print("Charlie")