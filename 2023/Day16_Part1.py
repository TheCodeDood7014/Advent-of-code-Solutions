with open("input.txt","r") as in_file:
    world = in_file.read().split("\n")
lights = [(-1,0,0)] # x, y, dire
start = True
# dire 0: right 1: down 2: left 3: up
# light simulation only stops when the light hits the edge.
x_size = len(world[0])
y_size = len(world)
visited = []
while True:
    # changed = True
    new_lights = []
    for light in lights:
        # The key to avoiding infinite loops is here: it would be best to record the dire in the light as well.
        # Because the intersection of this point BUT WITH DIFFERENT DIRES is acceptable
        # But same DIRES are not accepted
        if light not in visited and not start:
            visited.append(tuple(light)) # might as well do it here.
        else:
            if not start:
                continue
        light = list(light)
        if light[2] == 0:
            light[0] += 1
        elif light[2] == 1:
            light[1] += 1
        elif light[2] == 2:
            light[0] -= 1
        elif light[2] == 3:
            light[1] -= 1
        # if any of the x or y position is out of bounds, this case needs to be trashed.
        if not (0 <= light[0] < x_size and 0 <= light[1] < y_size) and not start:
            print(f"this case is not allowed: {light}")
            continue
        item = world[light[1]][light[0]]
        if item == '\\':
            # dire: 0 -> 1, 1 -> 0, 2 -> 3, 3 -> 2
            change = {0:1,1:0,2:3,3:2}
            new_lights.append(tuple(light[0:2]) + tuple([change[light[2]]]))
        elif item == '/':
            # dire: 0 -> 3, 3 -> 0, 1 -> 2, 2 -> 1
            change = {0:3,3:0,1:2,2:1}
            new_lights.append(tuple(light[0:2]) + tuple([change[light[2]]]))
        elif item == '|':
            # how to escape the infinite loop???
            # dire=1 or 3: doesn't change
            if light[2] % 2 == 1:
                new_lights.append(tuple(light))
            else:
                new_lights.append(tuple(light[0:2]) + tuple([1]))
                new_lights.append(tuple(light[0:2]) + tuple([3]))
        elif item == '-':
            # dire=0 or 2: doesn't change
            if light[2] % 2 == 0:
                new_lights.append(tuple(light))
            else:
                new_lights.append(tuple(light[0:2]) + tuple([2]))
                new_lights.append(tuple(light[0:2]) + tuple([0]))
        elif item == '.':
            new_lights.append(tuple(light))
        elif start:
            new_lights.append(tuple(light))
    if len(new_lights)==0:
        break
    lights = new_lights
    start = False
# just for diagnostic purpose
# I can't do len(set(visited)) as there could be the same positions, but with different dire
actual_visited = []
for x in visited:
    if x[0:2] not in actual_visited:
        actual_visited.append(x[0:2])
print(len(actual_visited))