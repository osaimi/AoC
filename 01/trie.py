from collections import defaultdict, deque


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.terminate = False
        self.value = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str, value: int):
        cur = self.root
        for char in word:
            cur = cur.children[char]
        cur.terminate = True
        cur.value = value

    def search(self, word: str) -> int | None:
        cur = self.root
        for char in word:
            cur = cur.children.get(char)
            if not cur:
                return None
        return cur.value if cur.terminate else None

    def starts_with(self, prefix: str) -> bool:
        cur = self.root
        for char in prefix:
            cur = cur.children.get(char)
            if not cur:
                return False
        return True


res = 0
nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
trie = Trie()
for i, num in enumerate(nums):
    trie.insert(num, i + 1)

with open('input', 'r') as file:
    lines = file.readlines()

for line in lines:
    left = right = 0
    d = deque()
    cur = None

    for char in line.strip():
        if char.isdigit():
            cur = int(char)
            d.clear()
        else:
            d.append(char)
            while d and not trie.starts_with("".join(d)):
                d.popleft()

            cur = trie.search("".join(d))

        if cur:
            left = left or cur
            right = cur

    res += left * 10 + right
print(res)
