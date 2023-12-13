import re
with open("input.txt","r") as in_file:
    content = [i.split("\n") for i in in_file.read().split("\n\n")]
def flip(i,x,y):
    if i[y][x] == '.':
        i[y] = i[y][:x] + '#' + i[y][x + 1:]
    elif i[y][x] == '#':
        i[y] = i[y][:x] + '.' + i[y][x + 1:]
    return i
def compare(a,b):
    # assuming len(a)=len(b)
    diff = 0
    for i,j in zip(a,b):
        if i!=j:
            diff += 1
    return diff
def find_all_mirror(grid, allow_diff):
    mirrors = []
    # Search for horizontals
    for i in range(1,len(grid)):
        # i denotes the reflection line is right above that row. e.g if i=1 then the line is above row 1
        # Find the sector with the least amount of rows
        min_sectorlen = min(len(grid) - i, i)
        flag = True
        # Repeat for rows i-min_sectorlen to (excluding) i, then i to i+min_sectorlen and compare differences.
        total_diff = 0
        for x in range(min_sectorlen):
            total_diff += compare(grid[i+x],grid[i-x-1])
        if total_diff == allow_diff: # I guess this is okay according to the subreddit (1 difference becoz of the smudge)
            return "r" + str(i) # Could just straight up return now
    # Search for verticals
    for i in range(1,len(grid[0])):
        # Find the sector with the least amount of cols
        min_sectorlen = min(len(grid[0]) - i, i)
        flag = True
        total_diff = 0
        for x in range(min_sectorlen): # Checkin' columns now
            total_diff += compare([grid[n][i-x-1] for n in range(len(grid))],[grid[n][i+x] for n in range(len(grid))])
        if total_diff == allow_diff:
            return "c" + str(i)
_sum = 0
for i in content:
    first_mirror = find_all_mirror(i,0) # Can only be one :D
    #print(first_mirror)
    # This time if no new reflection line is found then it will return None
    result = find_all_mirror(i,1)
    #print(result)
    if result[0] == 'r':
        _sum += 100 * int(re.findall("[0-9]+", result)[0])
        # Its a row
    elif result[0] == 'c':
        # Its a column
        _sum += int(re.findall("[0-9]+", result)[0])
    end = True
print(_sum)
# Turns our sometimes there can be multiple reflection lines. We only want the solution that only allows one