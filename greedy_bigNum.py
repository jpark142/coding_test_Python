n, m, k = map(int, input().split())

nums = list(map(int, input().split()))

nums.sort()

first_bigNum = nums[n-1]
second_bigNum = nums[n-2]

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        else:
            result += first_bigNum
            m -= 1
    if m == 0:
        break
    else:
        result += second_bigNum
        m -= 1

print(result)
