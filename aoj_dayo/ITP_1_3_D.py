a, b, c = map(int, input().split())
cnt = 0
while True:
    if a == (b+1):
        break
    if c % a == 0:
        cnt += 1
    a += 1
print(cnt)
