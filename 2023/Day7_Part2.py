# First find the type of hand.
# Then do sorts for each type group.

with open("input.txt","r") as in_file:
    content = [*map(lambda x: x.split(" "), in_file.read().split("\n"))]

# Find the type of each hand
# 0-6 for each type of hand starting from the strongest
def find_repeats(string, counts):
    #print(string)
    repeats = []
    for char in set(string):
        if string.count(char) == counts:
            repeats.append(char*counts)
    return repeats
def most_repeats(string):
    # First find the ones with max occurrences then find the max of those.
    max_val = 0
    max_chars = []
    for i in set(string):
        if i != 'J':
            result = string.count(i)
            if result > max_val:
                max_val = result
                max_chars = [i]
            elif result == max_val:
                max_chars.append(i)
    #print(string, max(max_chars))
    if len(max_chars) == 0:
        return '1'
    return max(max_chars)

def check_group(string):
    if len(find_repeats(string,5))!=0:
        # Five of a kind
        return 0
    if len(find_repeats(string,4))!=0:
        return 1
    result = find_repeats(string, 3)
    if len(result) !=0:
        result2 = find_repeats(string, 2)
        if len(result2) != 0:
            # Full house
            return 2
        else:
            # Three of a kind
            return 3
    result = find_repeats(string, 2)
    if len(result) == 2:
        return 4
    elif len(result) == 1:
        return 5
    return 6

def replace_jokers(hand):
    # The hand length is always 5 but yeah
    result = ""
    for i in range(5):
        if hand[i] == 'J':
            result += most_repeats(hand)
        else:
            result += hand[i]
    # This result is what will be when the joker is replaced.
    # Maybe determining what type of hand this (first) is will help with the problem
    # Then do ranking
    group = check_group(result)
    hand = hand.replace("J",'1') # Also helps alleviate this case: JJJJJ -> WEAK!!!
    return (group, hand)

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
    hand = hand.replace("T",'a').replace('Q','c').replace("K",'d').replace("A",'e')
    result = replace_jokers(hand)
    #print(hand, result)
    hands[result[0]].append((result[1], bid))

joined = []
# a c d e
# T Q K A
for key,value in hands.items():
    value.sort()
    value.reverse()
    joined += value
_sum = 0
#print(hands)
#print(list(reversed(joined)))
for count, hand in enumerate(reversed(joined)):
    # Rank = count + 1
    _sum += (count+1)*hand[1]
print(_sum)