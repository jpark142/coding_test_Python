n = int(input())

count = 0
#24시간 60분 60초
#하루는 총 86400초
for h in range(n+1):
    for m in range(60):
        for s in range(60):
            if '3' in str(h)+str(m)+str(s):
                count += 1

print(count)




