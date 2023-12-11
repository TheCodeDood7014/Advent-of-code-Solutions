import re
with open("input.txt","r") as in_file:
    content = [list(y) for y in in_file.read().split("\n")]

x_size = len(content[0])
y_size = len(content)
def expand_horiz():
    global content
    expand_lines = []
    for n, i in enumerate(content):
        if set(i) == {'.'}:
            # The entire row is empty
            expand_lines.append(n)
    for i in reversed(expand_lines):
        content.insert(i,list('.'*x_size))
def expand_vert():
    global content
    expand_columns = []
    for n in range(x_size):
        column = []
        for y in range(y_size):
            column .append(content[y][n])
        if set(column) == {'.'}:
            expand_columns.append(n)
    for i in reversed(expand_columns):
        for j in content:
            j.insert(i,'.')

expand_horiz()
# Now y_size has to be refreshed
y_size = len(content)
expand_vert()
galaxies = {}
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
#print(count)
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
