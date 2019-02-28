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
    f.close()


def findNext(chain):
    h_id = 0
    v_id = 0
    for i in range(len(h_pics)):
        interest = score(chain[-1], h_pics[i - 1])
        if interest >= max_interest:
            h_max_interest = interest

            h_id = i

    for j in range(len(v_pics)):
        interest = score(chain[-1], h_pics[i - 1])
        if interest >= max_interest:
            v_max_interest = interest
            v_id = i
    if v_max_interest < h_max_interest:
        chain.append(h_pics[h_id])
        h_pics.pop(h_id)
    else:
        chain.append(v_pic[v_id])
        v_pics.pop(v_id)
    return chain


def concatTags(Img1, Img2):
    return dict("id": str(Img1["id"] + " " + str(Img2["id"])), "o": "H", "nb_tags": len(
        Img1["tags"].union(Img2["tags"])), "tags": Img1["tags"].union(Img2["tags"]) )

def findNextVertical(chain):
    previous = chain[-2]
    max_interest = 0
    for i in range(len(v_pics)):
        previousvertical = chain[-1]
        concat_pic = concatTags(previousvertical, v_pics[i])
        interest = score(previous, concat_pic)
        if interest > max_interest:
            max_interest = interest
            new_picture = concat_pic
    chain.append(new_picture)

    return chain

def createChain():
    chain = [h_pics[0]]
    h_pics.pop(0)
    max_interest = 0

    # find the next picture with the highest score
    chain = findNext(chain)

    # Check if newly added picture is vertical
    if chain[-1]["o"] == "V":
        chain = findNextVertical(chain)


generateOutput(pics)
