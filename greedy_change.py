# 거슬러 줘야 할 돈이 1260원 일 때
N = 1260
count = 0
changes = [1000, 500, 100, 50, 10]

for i in changes:
    if N > i:
        count += N / i
    N = N % i


print(int(count))



