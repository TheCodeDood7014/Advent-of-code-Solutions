import re
from math import floor, ceil
content = """Time:        57     72     69     92
Distance:   291   1172   1176   2026""".split("\n")
times = re.findall("[0-9]+", content[0])
dists = re.findall("[0-9]+", content[1])
true_time = ""
for i in times:
    true_time += i
true_dist = ""
for i in dists:
    true_dist += i
# Formula for the distance: n(t-n) Where t is the number of seconds of the race and n is the # of seconds button
# is held
answer = 1
win_methods = 0
for n in range(0,int(true_time)//2):
    result = n*(int(true_time)-n)
    if result>int(true_dist):
        break

# We get the smallest n that can beat the record. So we do ways to win = (time/2 - n + 1)*2-1 apparently?
print((int(true_time)//2-n+1)*2-1)