import re
with open("input.txt","r") as f:
    grid = f.read().split("\n")

size = (len(grid[0]),len(grid))
gears = []
numbers = {}
ratios = 0
# For my input all the numbers are no more than 3 digits
for r,i in enumerate(grid):
    gears += [(x.span()[0],r) for x in re.finditer("\*",i)] # In the form (x,y)
    number_result = re.finditer("[0-9]+", i)
    for x in number_result:
        for n in [*zip(* [range(x.span()[0],x.span()[1])],[r for n in range(x.span()[1]-x.span()[0])])]:
            numbers[n] = int(x.group())
    # Form: (x1, y1), (x2+1, y2)

    # The righter x coordinate needs to be subtracted by 1
print(numbers)
print(gears)
for n in gears:
    check_area = [(n[0]-1,n[1]),(n[0]+1,n[1])] + [(n[0]+x, n[1]-1) for x in range(-1,2)] + [(n[0]+x, n[1]+1) for x in range(-1,2)]
    check_nums = []
    for x,y in check_area:
        if 0<=x<size[0] and 0<=y<=size[1]:
            if (x,y) in numbers.keys() and numbers[(x,y)] not in check_nums:
                print((x,y))
                check_nums.append(numbers[(x,y)])

    if check_nums.__len__() == 2:
        ratios += check_nums[0] * check_nums[1]

print(ratios)