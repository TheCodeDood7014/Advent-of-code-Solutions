# First find the type of hand.
# Then do sorts for each type group.

with open("input.txt","r") as in_file:
    content = [*map(lambda x: x.split(" "), in_file.read().split("\n"))]

# Find the type of each hand
# 0-6 for each type of hand starting from the strongest
def find_repeats(string, counts):
    for index, letter in enumerate(string):
        count = 1
        for j in range(1,counts):
            if index+j<len(string):
                if string[index+j] == letter:
                    count += 1
            else:
                break
        if count == counts:
            return True
    return False
def all_distinct(string):
    for i in range(len(string)):
        for j in range(i+1,len(string)):
            if string[i] == string[j]:
                return False
    return True

hands = {}
for i in range(7):
    hands[i] = []

for hand, bid in content:
    bid = int(bid)

    if find_repeats(hand,5):
        # Five of a kind
        hands[0].append((hand,bid))
        continue
    if find_repeats(hand,4):
        hands[1].append((hand,bid))
        continue
    result = find_repeats(hand, 3)
    if result:
        if find_repeats(hand.strip(result),2):
            hands[2].append((hand,bid))
        else:
            hands[3].append((hand,bid))
        continue
    result = find_repeats(hand, 2)
    if result:
        if find_repeats(hand.strip(result), 2):
            hands[4].append((hand,bid))
        else:
            hands[5].append((hand,bid))
        continue
    # There is no other left, must do this
    hands[6].append((hand,bid))

joined = []
for key,value in hands.items():
    value.sort()
    value.reverse()
    joined += value
_sum = 0
print(hands)
for count, hand in enumerate(reversed(joined)):
    # Rank = count + 1
    _sum += (count+1)*hand[1]
print(_sum)