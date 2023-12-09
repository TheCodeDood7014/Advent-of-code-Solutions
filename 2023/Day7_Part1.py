# First find the type of hand.
# Then do sorts for each type group.

with open("input.txt","r") as in_file:
    content = [*map(lambda x: x.split(" "), in_file.read().split("\n"))]

# Find the type of each hand
# 0-6 for each type of hand starting from the strongest
def find_repeats(string, counts):
    repeats = []
    for char in set(string):
        if string.count(char) == counts:
            repeats.append(char*counts)
    return repeats

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
    hand = hand.replace("T",'a').replace('J','b').replace('Q','c').replace("K",'d').replace("A",'e')
    if len(find_repeats(hand,5))!=0:
        # Five of a kind
        hands[0].append((hand,bid))
        continue
    if len(find_repeats(hand,4))!=0:
        hands[1].append((hand,bid))
        continue
    result = find_repeats(hand, 3)
    if len(result) !=0:
        result2 = find_repeats(hand, 2)
        if len(result2) != 0:
            # Full house
            hands[2].append((hand,bid))
            continue
        else:
            # Three of a kind
            hands[3].append((hand,bid))
            continue
    result = find_repeats(hand, 2)
    if len(result) == 2:
        hands[4].append((hand,bid))
        # Two pair
        continue
    elif len(result) == 1:
        hands[5].append((hand,bid))
        # One Pair
        continue
    hands[6].append((hand,bid))

joined = []
for key,value in hands.items():
    value.sort()
    value.reverse()
    joined += value
_sum = 0
print(hands)
print(joined)
for count, hand in enumerate(reversed(joined)):
    # Rank = count + 1
    _sum += (count+1)*hand[1]
print(_sum)