position = input()
can_move = 0

row = int(position[1])
col = int(ord(position[0]))-int(ord('a')) + 1

moving = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]


for i in moving:
    next_row = row + i[0]
    next_col = row + i[1]
    if next_row >= 1 and next_row <= 8 and next_col >= 1 and next_col <= 8:
        can_move += 1

print(can_move)





