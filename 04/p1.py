res = 0

with open('input', 'r') as file:
    for line in file:
        matches = 0
        _, cards = line.split(": ")
        winning, having = cards.split(" | ")
        winning = set([int(x) for x in winning.split()])
        having = [int(x) for x in having.split()]
        for num in having:
            if num in winning:
                matches += 1
        
        if matches:
            res += 2**(matches - 1)
print(res)
