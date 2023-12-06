with open('input', 'r') as file:
    matrix = [list(line.strip()) for line in file]

ROWS, COLS = len(matrix), len(matrix[0])

seq = 0
in_num = False
cur_num = []

map = {}

for r in range(ROWS):
    for c in range(COLS):
        char = matrix[r][c]
        if char.isdigit():
            if not in_num:
                in_num = True
            cur_num.append(char)
            matrix[r][c] = seq
        else:
            if in_num:
                in_num = False
                map[seq] = int("".join(cur_num))
                cur_num = []
                seq += 1

if in_num:
    map[seq] = int("".join(cur_num))

res = 0
dirs = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [-1, -1], [1, -1], [-1, 1]]
for r in range(ROWS):
    for c in range(COLS):
        char = matrix[r][c]
        nums = set()
        if char == "*":
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and isinstance(matrix[nr][nc], int):
                    nums.add(matrix[nr][nc])
        if len(nums) != 2:
            continue
        mul = 1
        for num in nums:
            mul *= map[num]
        res += mul

print(res)
