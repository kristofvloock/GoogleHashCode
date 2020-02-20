from math import ceil
filename = 'b_read_on.txt'

f = open(filename, 'r')
B, L, D = [int(i) for i in f.readline().strip('\n').split(' ')]
book_scores = [int(i) for i in f.readline().strip('\n').split(' ')]

libs = [] ###################
for l in range(L):
        nob, sup, rate =  [int(i) for i in f.readline().strip('\n').split(' ')]
        books = [int(i) for i in f.readline().strip('\n').split(' ')]
        scan_days = ceil(nob/rate)
        lib = {
            'nob': nob,
            'sup': sup,
            'rate': rate,
            'books': books,
            'scan_days': int(ceil(nob/rate))
        }
        libs.append(lib)