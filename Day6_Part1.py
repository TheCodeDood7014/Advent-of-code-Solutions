import re
from math import floor, ceil
content = """Time:        57     72     69     92
Distance:   291   1172   1176   2026""".split("\n")
times = [*map(int,re.findall("[0-9]+", content[0]))]
dists = [*map(int,re.findall("[0-9]+", content[1]))]
# Formula for the distance: -n(n-t) Where t is the number of seconds of the race and n is the # of seconds button
# is held
answer = 1
for t, d in zip(times,dists):
    win_methods = 0
    for n in range(1,t):
        result = n*(t-n)
        if result>d:
            win_methods += 1
    answer *= win_methods
print(answer)