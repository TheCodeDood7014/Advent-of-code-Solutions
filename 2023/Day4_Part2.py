def filter(x):
    result = []
    for i in x:
        if i != '':
            result.append(i)
    return result


def intersect(x, y):
    result = []
    for i in x:
        if i in y:
            result.append(i)
    return result


with open("input.txt", "r") as in_file:
    content = [[[int(x) for x in filter(j.replace("  ", " ").split(" "))] for j in i[10:].split(" | ")] for i in
               in_file.read().split("\n")]

cards = len(content)
card_wins = [0 for i in range(cards)]
instances = [1 for i in range(cards)]
for count, lists in enumerate(content):
    w = lists[0]
    n = lists[1]
    wins = len(list(set(w).intersection(set(n))))
    card_wins[count] = wins

for i,j in enumerate(instances): # Loop through the cards 1-209
    for a in range(card_wins[i]): # Add the copies based on the number of wins of that card
        instances[i+a+1] += j # Added to instances.

print(sum(instances))