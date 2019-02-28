import numpy as np
from itertools import permutations
from itertools import combinations


f = open('b_lovely_landscapes.txt', 'r')

N = int(f.readline().strip('\n'))
print(N)

data = [[char for char in line.strip('\n').split(' ')] for line in f.readlines()]

pics = []

id = 0

for pic in data:
    d = {'id': id, 'o': pic[0], 'nb_tags': int(pic[1]), 'tags': set(pic[2:])}
    pics.append(d)
    id += 1


def score(Img1, Img2):
    identical = 0
    for tag in Img1["tags"]:
        for tag2 in Img2["tags"]:
            if tag == tag2:
                identical += 1
    return min(identical, Img1["nb_tags"] - identical, Img2["nb_tags"] - identical)


def total_score(photos):
    t_score = 0
    for i in range(len(photos) - 1):
        t_score += score(photos[i], photos[i+1])
    return t_score

# print(list(combinations([i for i in pics if i['o'] == 'V'], 2)))

print("GEnerating list")
all_combos = list(permutations(pics))
max_score = 0
i=0

print("Start forcing")
for combo in all_combos:
    print(i)
    current_score = total_score(combo)
    if current_score > max_score:
        max_score = current_score
        best = combo
    i += 1

print("max score", max_score)
print(best)