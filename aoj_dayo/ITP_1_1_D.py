S = int(input())
a = S // 3600
b = S % 3600
c = b // 60
d = b % 60
print(f"{a}:{c}:{d}")
