n, m = map(int, input().split())
x, y, direction = map(int, input().split())

m_map = [[0]*m for _ in range(n)]

# 현재 좌표 방문상태로 처리
m_map[x][y] = 1

# 전체 맵 입력받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북 동 남 서 방향
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽 방향으로 몸 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 시뮬레이션 시작
count = 1
turn_time = 0

while True:
    turn_left()
    new_x = x + dx[direction]
    new_y = y + dy[direction]

    # 만약에 가보지 않은 길이라면
    if m_map[new_x][new_y] == 0 and array[new_x][new_y] == 0:
        m_map[new_x][new_y] = 1
        x = new_x
        y = new_y
        count += 1
        turn_time = 0
        continue
    # 가본 길이거나 앞이 바다인 경우
    else:
        turn_time += 1

    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        new_x = x - dx[direction]
        new_y = y - dy[direction]
        if array[new_x][new_y] == 0:
            x = new_x
            y = new_y
        else:
            break
        turn_time = 0

print(count)




