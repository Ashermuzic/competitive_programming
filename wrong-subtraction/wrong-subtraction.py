n, k = list(map(int,input().split()))

for _ in range(k):
    if str(n)[-1] == "0":
        n = n // 10
    else:
        n = n - 1
print(n)
