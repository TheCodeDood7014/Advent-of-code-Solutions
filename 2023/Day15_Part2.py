import re
with open("input.txt","r") as in_file:
    steps = in_file.read().split(",")
def hash(x):
    code = 0
    for i in x:
        code += ord(i)
        code *= 17
        code %= 256
    return code
boxes = dict([(i, []) for i in range(256)])
for i in steps:
    box_number = hash(re.findall("[a-z]+",i)[0])
    # Now, depending on the operation we do different stuff
    # Also if it's - we don't have to search every box for that lens.
    if i.find("=") != -1:
        # Also gotta check if a lens with this label exists
        new_len = tuple(i.split("="))
        found=False
        for i, j in enumerate(boxes[box_number]):
            if new_len[0] == j[0]:
                boxes[box_number][i] = new_len
                found = True
                break
        if not found:
            boxes[box_number].append(new_len)
    elif i.find("-") != -1:
        lens_label = i.replace("-","")
        # Now search for that lens
        for index, x in enumerate(boxes[box_number]):
            if x[0] == lens_label:
                del boxes[box_number][index]
focal_power= 0
for key,value in boxes.items():
    # key is box number
    # value is the lens installed, in order...
    for slot, lens in enumerate(value):
        focal_power += (key+1)*(slot+1)*int(lens[1])
print(focal_power)