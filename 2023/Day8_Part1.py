with open("input.txt","r") as in_file:
    content = in_file.read().split("\n\n")
    instructions = content[0]
    node_input = [i.split(" = ") for i in content[1].split("\n")]
    nodes = dict()
    for i, j in node_input:
        nodes[i] = tuple(j.replace("(","").replace(")","").split(", "))
position = 'AAA'
instruction_index = 0
while position != 'ZZZ':
    inst = instructions[instruction_index%len(instructions)]
    if inst == 'L':
        position = nodes[position][0]
    else:
        position = nodes[position][1]
    instruction_index += 1
print(instruction_index)