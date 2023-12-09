def filter(x):
    result = []
    for i in x:
        if i != '':
            result.append(i)
    return result
def intersect(x,y):
    result = []
    for i in x:
        if i in y:
            result.append(i)
    return result
with open("input.txt","r") as in_file:
    content = [[[int(x) for x in filter(j.replace("  "," ").split(" "))] for j in i[10:].split(" | ")] for i in in_file.read().split("\n")]
score = 0
for w,n in content:
    #intersects = intersect(w,n)
    intersects = list(set(w).intersection(set(n)))
    print(w,n,intersects)
    result = len(intersects)
    add_score = 2 ** (result-1)
    print(result)
    if result != 0:
        score +=add_score
print(score)
