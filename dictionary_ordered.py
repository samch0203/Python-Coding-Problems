from collections import OrderedDict

n = int(input())
items = OrderedDict()

for _ in range(n):
    line = input().split()
    item_name = " ".join(line[:-1])
    price = int(line[-1])

    if item_name in items:
        items[item_name] += price
    else:
        items[item_name] = price

for item, total in items.items():
    print(item, total)
