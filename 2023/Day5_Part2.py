def find_range_overlap(x, y):
    return range(max(x[0], y[0]), min(x[-1], y[-1])+1)
def snip_range(rangea, rangeb):
    return (range(rangea.start,rangeb.start),range(rangeb.stop, rangea.stop))
with open("input","r") as in_file:
    maps = in_file.read().split("\n\n")
    seeds = [*map(int, maps[0].split(" ")[1:])]
    seed_ranges = []
    for i in range(len(seeds) // 2):
        seed_ranges.append(range(seeds[2 * i], seeds[2 * i] + seeds[2 * i + 1]))
    for n,map in enumerate(maps[1:]):
        maps[n+1] = [[int(j) for j in i.split(" ")] for i in map.split("\n")[1:]]
# Mapping destination, Mapping source, Mapping Length
# At mapping source map the values (starting from Mapping destination) for Mapping Length values.
for num_maps in range(1,8):
    # Make the ranges
    print(num_maps)
    ranges = []
    for i in maps[num_maps]:
        ranges.append((i[0], range(i[1],i[1]+i[2],1)))
    parsed = []
    for num,i in enumerate(seed_ranges):
        found_match =False
        for x in ranges:
            result = find_range_overlap(x[1],i)
            if len(result) == 0 :
                continue
                #seed_ranges = parsed
            else:
                # If an overlap is found, remap THE OVERLAP, then write to the list "parsed".
                found_match = True
                range_start = x[1].index(result.start) + x[0]
                # Append the parsed "result" range. To find the length of it we can check the length of the result
                parsed.append(range(range_start,range_start+result.stop-result.start))
                #seeds[num] = x[1].index(i.start) + x[0] # Needs to be changed. We have to write a range not a num
                result = snip_range(i,result) # Problem here - what if there is entire overlap?
                if len(result[0]) != 0:
                    seed_ranges.append(result[0])
                if len(result[1]) != 0:
                    seed_ranges.append(result[1])
                break
        # Didn't consider the fact that if it is not mapped the value stays the same
        if not found_match:
            parsed.append(i)
    #print(parsed)
    seed_ranges = parsed

# Now that we have a bunch of result ranges get the minimum now.
print("Finding Minimum")
result = []
for i in seed_ranges:
    result.append(i.start)
#print(result)
print(min(result))
