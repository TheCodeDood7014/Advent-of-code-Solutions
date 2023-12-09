with open("input.txt","r") as in_file:
    content = [*map(lambda x: x.split(" "), in_file.read().split('\n'))]
def find_degree(x):
    diff = []
    for i in range(len(x)-1):
        diff.append(int(x[i+1])-int(x[i]))
    if len(set(diff)) == 1:
        # That means we have reached the bottom
        return 1
    return 1+find_degree(diff)
def find_next_term(x,degree):
    # We can use the difference method to find the next term
    deltas = {0:x}
    for deg in range(1,degree+1):
        diff = []
        for i in range(len(x)-1):
            diff.append(int(x[i+1])-int(x[i]))
        deltas[deg] = diff
        if len(set(diff)) == 1:
            # That means we have reached the bottom
            # So now we can append to the delta-<deg> list
            # And then begin process of finding the next term
            break
        else:
            x = diff
    deltas[degree].append(deltas[degree][-1])
    for i in range(len(deltas)-1,-1+1,-1): # Go backwards
        deltas[i-1].append(deltas[i][-1]+int(deltas[i-1][-1]))
    return deltas[0][-1]

_sum = 0
for i in content:
    degree = find_degree(i)
    _sum += find_next_term(i,degree)
print(_sum)