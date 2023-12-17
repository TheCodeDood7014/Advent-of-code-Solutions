import re
def join_string(x):
    _str = ""
    for i in x:
        _str += i
    return _str
def roll(dire):
    if dire % 2 == 0:
        if dire == 0:
            for row, i in enumerate(content[1:-1]):
                # row should be row + 1
                row = row + 1
                rocks = [(x.span()[0], row) for x in re.finditer("O", join_string(i))]
                # x doesn't change
                for rock in rocks:
                    # Make it continuously roll until it hits '#' or 'O'
                    y = row
                    while content[y - 1][rock[0]] not in ['#', 'O']:
                        y -= 1
                    content[rock[1]][rock[0]] = '.'
                    content[y][rock[0]] = 'O'
        elif dire == 2:
            for row, i in enumerate(reversed(content[1:-1])):
                # row should be row + 1
                row = y_size - (row + 1)-1
                rocks = [(x.span()[0], row) for x in re.finditer("O", join_string(i))]
                # x doesn't change
                for rock in rocks:
                    # Make it continuously roll until it hits '#' or 'O'
                    y = row
                    while content[y + 1][rock[0]] not in ['#', 'O']:
                        y += 1
                    content[rock[1]][rock[0]] = '.'
                    content[y][rock[0]] = 'O'
    elif dire % 2 == 1:
        if dire == 1:
            for column, i in enumerate(reversed([[content[y][x] for y in range(y_size)] for x in range(1,x_size-1)])):
                # True column = column + 1
                column = x_size - (column + 1)-1
                # Find rollin' rocks in that column (i is dat column)
                rocks = [(column, x.span()[0]) for x in re.finditer("O", join_string(i))]
                for rock in rocks:
                    # Make it continuously roll until it hits '#' or 'O'
                    x = column
                    while content[rock[1]][x+1] not in ['#', 'O']:
                        x += 1
                    content[rock[1]][rock[0]] = '.'
                    content[rock[1]][x] = 'O'
        elif dire == 3:
            for column, i in enumerate([[content[y][x] for y in range(y_size)] for x in range(1,x_size-1)]):
                # True column = column + 1
                column = column + 1
                # Find rollin' rocks in that column (i is dat column)
                rocks = [(column, x.span()[0]) for x in re.finditer("O", join_string(i))]
                for rock in rocks:
                    x = column
                    while content[rock[1]][x - 1] not in ['#', 'O']:
                        x -= 1
                    # Now just update content
                    content[rock[1]][rock[0]] = '.'
                    content[rock[1]][x] = 'O'
with open("input.txt", "r") as in_file:
    content = [list(x) for x in in_file.read().split("\n")]
    # Might be easier NOT to store it as strings, but as chars
    x_size = len(content[0])
    y_size = len(content)
    content.insert(0,["#"]*x_size)
    content.append(["#"] * x_size)
    for i in content:
        i.insert(0,'#')
        i.append("#")
    x_size += 2
    y_size += 2

# 1 cycle. 1 BILLION!? Well, Time to use Repeating occurrences!
initial = [tuple(i) for i in content]
# for x in initial:
#     print(join_string(x))
counter = 1 # because how my program is made I have to do this
seen = dict()
jumped = False
while True:
    if counter == 1_000_000_000:
        break
    for dire in [0,3,2,1]:
        roll(dire)
    temp = tuple([tuple(x) for x in content])
    if temp not in list(seen.keys()):
        seen[temp] = counter # First time we see that
        counter += 1
    else:
        if not jumped:
            # That means we have seen this for the second time.
            # The repeat time is counter-seen[content]
            repeat_time = counter - seen[temp]
            # cause we kinda know this pattern will show up again after a set amount of time.
            # Therefore... we can do a TIME JUMP!
            counter = counter + repeat_time*((1_000_000_000-counter)//repeat_time)
            jumped = True
        else:
            counter += 1
    #print(counter)
# Now calculate load, I guess
load = 0
for row_num, row_content in enumerate(content[1:-1]):
    rocks = row_content.count("O")
    load += ((y_size-2)-row_num)*rocks
print(load)