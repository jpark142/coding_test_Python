size = int(input())
x, y = 1, 1
direction = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move = ['L', 'R', 'U', 'D']

for d in direction:
    for i in range(len(move)):
        if d == move[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > size or ny > size:
        continue

    x, y = nx, ny

print(x, y)



