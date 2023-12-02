res = 0

with open('input', 'r') as file:
    lines = file.readlines()

for line in lines:
    left = right = 0
    for char in line.strip():
        if char.isdigit():
            digit = int(char)
            left = left if left != 0 else digit
            right = digit

    res += left * 10 + right

print(res)
