import re

t = int(input())

for _ in range(t):
    number = input().strip()

    if re.fullmatch(r'[789]\d{9}', number):
        print("YES")
    else:
        print("NO")
