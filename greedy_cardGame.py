n, m = map(int, input().split())

result = 0
for i in range(n):
    nums = list(map(int, input().split()))
    min_num = min(nums)
    result = max(result, min_num)

print(result)
