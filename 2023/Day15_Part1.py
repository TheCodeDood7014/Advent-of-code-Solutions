with open("input.txt","r") as in_file:
    steps = in_file.read().split(",")
def hash(x):
    code = 0
    for i in x:
        code += ord(i)
        code *= 17
        code %= 256
    return code
values = []
for i in steps:
    values.append(hash(i))
print(sum(values))