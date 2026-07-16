from collections import defaultdict

n, m = map(int, input().split())

d = defaultdict(list)

# Read Group A
for i in range(1, n + 1):
    word = input()
    d[word].append(i)

# Read Group B and print results
for _ in range(m):
    word = input()
    if word in d:
        print(*d[word])
    else:
        print(-1)
