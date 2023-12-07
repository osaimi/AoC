import collections

count = collections.defaultdict(int)

with open('input', 'r') as file:
    matrix = [row.strip() for row in file]

length = len(matrix)
for i, line in enumerate(matrix):
    count[i] += 1

    matches = 0
    _, cards = line.split(": ")
    winning, having = cards.split(" | ")
    winning = set([int(x) for x in winning.split()])
    having = [int(x) for x in having.split()]
    for num in having:
        if num in winning:
            matches += 1

    if matches:
        for j in range(i + 1, min(i + 1 + matches, length)):
            count[j] += count[i]
print(sum(count.values()))
