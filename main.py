import numpy as np
from itertools import permutations
from itertools import combinations


f = open('e_shiny_selfies.txt', 'r')

N = int(f.readline().strip('\n'))
print(N)

data = [[char for char in line.strip('\n').split(' ')] for line in f.readlines()]

pics = []

id = 0

for pic in data:
    d = {'id': id, 'o': pic[0], 'nb_tags': int(pic[1]), 'tags': set(pic[2:])}
    pics.append(d)
    id += 1

v_pics = [pic for pic in pics if pic['o'] == 'V']
h_pics = [pic for pic in pics if pic['o'] == 'H']

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

def generateOutput(slideshow):
    f = open('submission.txt', 'w')
    f.write(str(len(slideshow)) + '\n')
    for p in slideshow:
        if p != slideshow[-1]:
            f.write(str(p['id']) + '\n')
        else:
            f.write(str(p['id']))

generateOutput(pics)
