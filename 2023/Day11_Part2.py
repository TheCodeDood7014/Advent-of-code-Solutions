import re
with open("input.txt","r") as in_file:
    content = [list(y) for y in in_file.read().split("\n")]

x_size = len(content[0])
y_size = len(content)
galaxies = dict()
# Now search for galaxies
count = 0
for r, i in enumerate(content):
    string =""
    for x in i:
        string += x
    result = [x.span()[0] for x in re.finditer("#",string)]
    for x in result:
        galaxies[count] = [x,r]
        count += 1
def expand_horiz():
    global galaxies
    expand_lines = []
    for n, i in enumerate(content):
        if set(i) == {'.'}:
            # The entire row is empty
            expand_lines.append(n)
    for i in reversed(expand_lines):
        for n, coor in enumerate(galaxies.items()):
            if coor[1][1] > i:
                galaxies[n][1] += 999999
    return len(expand_lines)

def expand_vert():
    global galaxies
    expand_columns = []
    for n in range(x_size):
        column = []
        for y in range(y_size):
            column .append(content[y][n])
        if set(column) == {'.'}:
            expand_columns.append(n)
    for i in reversed(expand_columns):
        for n, coor in enumerate(galaxies.items()):
            if coor[1][0] > i:
                galaxies[n][0] += 999999

expand_horiz()
# Now y_size has to be refreshed
expand_vert()
#y_size += 10*res
# Now loop through the pairs
distances = []
for n, i in enumerate(galaxies.items()):
    for x in range(1+n,len(galaxies)):
        # Get distance
        g_id, coor = i
        #print(galaxies[x],coor)
        distance = abs(coor[1]-galaxies[x][1])+abs(coor[0]-galaxies[x][0])
        #print("{} and {}: {}".format(n+1,x+1,distance))
        distances.append(distance)
print(sum(distances))
