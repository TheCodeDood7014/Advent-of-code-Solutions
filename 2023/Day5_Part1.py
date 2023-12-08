with open("input.txt","r") as in_file:
    maps = in_file.read().split("\n\n")
    seeds = [*map(int,maps[0].split(" ")[1:])]
    for n,map in enumerate(maps[1:]):
        maps[n+1] = [[int(j) for j in i.split(" ")] for i in map.split("\n")[1:]]
# Mapping destination, Mapping source, Mapping Length
# At mapping source map the values (starting from Mapping destination) for Mapping Length values.

for num_maps in range(1,8):
    # Make the ranges
    ranges = []
    for i in maps[num_maps]:
        ranges.append((i[0], range(i[1],i[1]+i[2],1)))
    for num,i in enumerate(seeds):
        for x in ranges:
            if i in x[1]:
                seeds[num] = x[1].index(i)+x[0]
                break
print(min(seeds))
