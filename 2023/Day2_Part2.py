import re
with open("input.txt","r") as f:
    content = []
    for n,i in enumerate(f.read().split("\n")):
        content.append( i[(len(str(n+1)) + 7):].split("; ") )
def verify(x,c):
    # c: number of chars in the color name
    if x == []:
        x = 0
    else:
        x = int(x[0][:-c-1])
    return x
sum_powers = 0
for n, i in enumerate(content): # Go for each item in the content. A.k.a. each game
    min_r, min_g, min_b = 0,0,0
    for x in i:
        r,g,b = verify(re.findall("[0-9]+ red", x),3), verify(re.findall("[0-9]+ green", x),5),verify(re.findall("[0-9]+ blue", x),4)
        if r >= min_r:
            min_r = r
        if g >= min_g:
            min_g = g
        if b >= min_b:
            min_b = b
    sum_powers += min_r*min_g*min_b

print(sum_powers)