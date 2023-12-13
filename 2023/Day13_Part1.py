import re
with open("input.txt","r") as in_file:
    content = [i.split("\n") for i in in_file.read().split("\n\n")]
def find_mirror(grid):
    # Search for horizontals
    for i in range(1,len(grid)):
        # i denotes the reflection line is right above that row. e.g if i=1 then the line is above row 1
        # Find the sector with the least amount of rows
        min_sectorlen = min(len(grid) - i, i)
        flag = True
        for column in range(len(grid[0])):
            tuple1 = tuple([grid[y][column] for y in range(i-min_sectorlen,i)])
            tuple2 = tuple([grid[y][column] for y in range(i,i+min_sectorlen)])
            if tuple1 != tuple(reversed(tuple2)):
                flag = False
                break
        # If loop ends this is a reflection line
        if flag:
            return "r" + str(i)
        else:
            continue
    # Search for verticals
    for i in range(1,len(grid[0])):
        # Find the sector with the least amount of cols
        min_sectorlen = min(len(grid[0]) - i, i)
        flag = True
        for row in range(len(grid)):
            tuple1 = tuple([grid[row][x] for x in range(i - min_sectorlen, i)])
            tuple2 = tuple([grid[row][x] for x in range(i, i + min_sectorlen)])
            if tuple1 != tuple(reversed(tuple2)):
                flag = False
                break
        if flag:
            return "c" + str(i)
        else:
            continue
#print(find_mirror(content[0])) # Luckily what it returns exactly the answer we want!
_sum = 0
for i in content:
    result = find_mirror(i)
    if result[0] == 'r':
        _sum += 100*int(re.findall("[0-9]+",result)[0])
        # Its a row
    elif result[0] == 'c':
        # Its a column
        _sum += int(re.findall("[0-9]+", result)[0])
print(_sum)