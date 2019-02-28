import numpy as np

f = open('a_example.txt', 'r')

N = int(f.readline().strip('\n'))

data = [[char for char in line.strip('\n').split(' ')] for line in f.readlines()]

pics = []

id = 0

for pic in data:
    d = {'id': id, 'o': pic[0], 'nb_tags': int(pic[1]), 'tags': pic[2:]}
    pics.append(d)
    id += 1

