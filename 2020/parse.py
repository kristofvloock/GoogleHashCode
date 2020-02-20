from math import ceil
import sys

filename = sys.argv[1]

f = open(filename, 'r')
B, L, D = [int(i) for i in f.readline().strip('\n').split(' ')]
book_scores = [int(i) for i in f.readline().strip('\n').split(' ')]

libs = [] ###################
for l in range(L):
        nob, sup, rate =  [int(i) for i in f.readline().strip('\n').split(' ')]
        books = [int(i) for i in f.readline().strip('\n').split(' ')]
        scan_days = ceil(nob/rate)
        lib = {
            'id': l,
            'nob': nob,
            'sup': sup,
            'rate': rate,
            'books': books,
            'scan_days': int(ceil(nob/rate)),
            'sign_order': None,
            'amo_scanned_books': None,
            'scanned_books': None
        }
        libs.append(lib)

def generateOutput(output_libs):
    global filename
    f = open(filename + '_sol.txt', 'w')
    f.write(str(len(output_libs))+ '\n')
    
    for out_lib in output_libs:
        f.write(str(out_lib['id']) + ' ' + str(out_lib['amo_scanned_books']) + '\n')
        out_books = "".join([str(b) + ' ' for b in out_lib['scanned_books']])[:-1]
        f.write(out_books + '\n')
    f.close()

generateOutput(libs)
