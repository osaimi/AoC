res = 0

with open('input', 'r') as file:
    lines = file.readlines()

nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

for line in lines:
    left = right = 0
    for i, char in enumerate(line.strip()):
        if char.isdigit():
            digit = int(char)
            left = left if left != 0 else digit
            right = digit
        else:
            for j, num in enumerate(nums):
                if line[i:(i + len(num))] == num:
                    digit = j + 1
                    left = left if left != 0 else digit
                    right = digit
                    break


    res += left * 10 + right

print(res)
