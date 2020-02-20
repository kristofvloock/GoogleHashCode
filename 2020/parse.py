filename = 'a_example.txt'

f = open(filename, 'r')
B, L, D = f.readline().strip('\n').split(' ')

print(header)