with open('input', 'r') as file:
    lines = file.readlines()

limits = {
    'red': 12,
    'green': 13,
    'blue': 14
}

res = 0
for line in lines:
    s_id, s_cubes = line.split(":")
    game_id = int(s_id.split(" ")[1])
    sets = s_cubes.strip().split(";")
    valid = True

    for st in sets:
        st = st.split(",")
        for r in st:
            count, color = r.strip().split(" ")
            if limits[color] < int(count):
                valid = False
                break
                ...
        if not valid:
            break
    if valid:
        res += game_id

print(res)
