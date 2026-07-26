import re

T = int(raw_input())

for _ in range(T):
    pattern = raw_input()
    try:
        re.compile(pattern)
        print "True"
    except re.error:
        print "False"
