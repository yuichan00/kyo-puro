
while True:
    x, y = map(int, input().split())
    if x == 0 and y == 0:
        break
    if x < y:
        print(x, y)
    elif y < x:
        print(y, x)
    else:
        print(x, y)
