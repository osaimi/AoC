with open('input', 'r') as file:
    lines = file.readlines()


res = 0
for line in lines:
    s_id, s_cubes = line.split(":")
    game_id = int(s_id.split(" ")[1])
    sets = s_cubes.strip().split(";")
    valid = True
    needed = {
        'red': float('-inf'),
        'blue': float('-inf'),
        'green': float('-inf')
    }

    for st in sets:
        st = st.split(",")
        for r in st:
            count, color = r.strip().split(" ")
            needed[color] = max(needed[color], int(count))

    for color in needed.keys():
        if needed[color] == float('-inf'):
            needed[color] = 1

    res += needed['red'] * needed['blue'] * needed['green']
print(res)
