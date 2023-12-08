import math
def verify_pos(positions):
    for i in positions:
        if i[-1] != 'Z':
            return False
    return True
with open("input.txt","r") as in_file:
    content = in_file.read().split("\n\n")
    instructions = content[0]
    node_input = [i.split(" = ") for i in content[1].split("\n")]
    nodes = dict()
    for i, j in node_input:
        nodes[i] = tuple(j.replace("(","").replace(")","").split(", "))
positions = []
for i in nodes.keys():
    if i[-1] == 'A':
        positions.append(i)

# The number of notes ending with A = the number of nodes ending with Z
steps = []
for x in positions:
    # Find the amount of steps to reach the Z.
    inst_index = 0
    sub_pos = x
    while sub_pos[-1] != 'Z':
        inst = instructions[inst_index % len(instructions)]
        if inst == 'L':
            sub_pos = nodes[sub_pos][0]
        else:
            sub_pos = nodes[sub_pos][1]
        if sub_pos[-1] == 'Z':
            # This+1 is the amount of steps to reach Z
            steps.append(inst_index+1)
            break
        else:
            inst_index += 1

# Find LCM of steps
print(steps)
print("Finding LCM")
print(math.lcm(*steps))