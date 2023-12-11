from math import ceil
with open("input.txt","r") as in_file:
    content = in_file.read().split("\n")
    for r, i in enumerate(content):
        result = i.find("S")
        if result != -1:
            start_pos = [result,r]
def replace_s(char,s_pos):
    temp = content[s_pos[1]].split("S")
    content[s_pos[1]] = temp[0] + char + temp[1]
path_left = content[start_pos[1]][start_pos[0]-1] in ["-","F","L"]
path_right = content[start_pos[1]][start_pos[0]+1] in ["-","J","7"]
path_up = content[start_pos[1]-1][start_pos[0]] in ["|","F","7"]
path_down = content[start_pos[1]+1][start_pos[0]] in ["|","J","L"]
if path_left and path_right:
    replace_s('-',start_pos)
elif path_up and path_down:
    replace_s('|',start_pos)
elif path_left and path_down:
    replace_s('7',start_pos)
elif path_left and path_up:
    replace_s('J',start_pos)
elif path_right and path_down:
    replace_s('F',start_pos)
else:
    replace_s('L',start_pos)

x_size = len(content[0])
y_size = len(content)
# Let's trace the loop
def get(x,y):
    return content[y][x]
def get2(pos):
    return content[pos[1]][pos[0]]
def trace():
    loop = []
    cur_pos = start_pos
    while True:
        loop.append(tuple(cur_pos))
        # Can we go right?
        if cur_pos[0]+1<x_size and get2(cur_pos) in ['-','F','L'] and get(cur_pos[0]+1,cur_pos[1]) in ['-','J','7'] and (cur_pos[0]+1,cur_pos[1]) not in loop:
            # Ye we can
            cur_pos[0] += 1
        # Can we go left?
        elif cur_pos[0]-1>=0 and get2(cur_pos) in ['-','J','7'] and get(cur_pos[0]-1,cur_pos[1]) in ['-','F','L'] and (cur_pos[0]-1,cur_pos[1]) not in loop:
            # Ye we can!
            cur_pos[0] -= 1
        # Up?
        elif cur_pos[1]-1>=0 and get2(cur_pos) in ['|','J','L'] and get(cur_pos[0],cur_pos[1]-1) in ['|','F','7'] and (cur_pos[0],cur_pos[1]-1) not in loop:
            # Ye we can!
            cur_pos[1] -= 1
        # Down?
        elif cur_pos[1]+1<y_size and get2(cur_pos) in ['|','F','7'] and get(cur_pos[0],cur_pos[1]+1) in ['|','J','L'] and (cur_pos[0],cur_pos[1]+1) not in loop:
            # Ye we can
            cur_pos[1] += 1
        else:
            # That's the end of the loop
            return loop
            break

loop = trace()
new_loop = []
print("Part 1: {}".format(ceil(len(loop)//2)))
for i in loop:
    if get2(i) in ['|','J','L']: # WHY??????
        new_loop.append(i)

# Now use the parity tracing method to find inscribed points
# First find min and max of points
x_cords,y_cords = zip(*loop)
# We do horizontal trace?
inscribed = 0
for x in range(min(x_cords),max(x_cords)+1):
    for y in range(min(y_cords),max(y_cords)+1):
        # Do horizontal trace
        intersect = {(i,y) for i in range(0,x+1)}.intersection(set(new_loop))
        #print((x, y), list(sorted(intersect)), len(intersect))
        if len(intersect)%2 == 1 and (x,y) not in loop:
            # It's inside
            #print(x,y)
            inscribed += 1
print("Part 2: {}".format(inscribed))