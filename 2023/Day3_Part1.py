import re
with open("input.txt","r") as f:
    grid = f.read().split("\n")

size = (len(grid[0]),len(grid))
part_nums = 0
for r,i in enumerate(grid):
    result = [x.span() for x in re.finditer("[0-9]+",i)] # get the left most position of each number.
    for n in result:
        part = eval(grid[r][n[0]:n[1]])
        length = n[1]-n[0] # Removed the +1 for a reason
        # Checking area coords are in the form (x,y) not (r,c)
        areas = [(n[0]-1,r),(n[1]+1-1,r)] + [(n[0]+x,r-1) for x in range(-1,length+1)] + [(n[0]+x,r+1) for x in range(-1,length+1)]
        for x,y in areas:
            if 0 <= x < size[0] and 0 <= y < size[1]:
                if grid[y][x] not in list("0123456789."):
                    part_nums += part
                    break
print(part_nums)