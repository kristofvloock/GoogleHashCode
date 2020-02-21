from math import ceil
import sys
from score import *
import numpy as np

filename = sys.argv[1]

f = open(filename, 'r')
B, L, D = [int(i) for i in f.readline().strip('\n').split(' ')]
book_scores = [int(i) for i in f.readline().strip('\n').split(' ')]

libs = []
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
            'amo_scanned_books': 0,
            'scanned_books': []
        }
        libs.append(lib)

in_signup = False
signup_period = -1
lib_signup = []
ready_to_scan = []
sorted_ready_libs = []
signed_libs = libs[:]
for day in range(1, D + 1):
    if signup_period == 0:
        in_signup = False
        ready_to_scan.append(lib_signup[-1])

        books = libs[lib_signup[-1]]['books']
        book_score_list = [book_scores[i] for i in books]
        sorted_books = [book for _,book in sorted(zip(book_score_list,books))]
        sorted_ready_libs.append(sorted_books)
        libs[lib_signup[-1]]['books'] = sorted_books
        
    if not in_signup and len(lib_signup) != len(libs):
        avg_scores = avg_score(signed_libs, book_scores)
        lib_scores = lib_score(D, day, signed_libs, avg_scores)

        sorted_idx = np.argsort(lib_scores)[::-1]
        lib_to_sign_up = signed_libs.pop(sorted_idx[0])['id']
        lib_signup.append(lib_to_sign_up)
        signup_period = libs[lib_to_sign_up]['sup']
        in_signup = True
        
    for i,lib in enumerate(ready_to_scan):
        scan_rate = libs[lib]['rate']
        scanned = []
        for j in range(scan_rate):
            if len(libs[lib]['books']) == 0:
                ready_to_scan = ready_to_scan[:i]+ready_to_scan[i+1:]
                i -= 1
                break
            scanned.append(libs[lib]['books'].pop(-1))
        libs[lib]['scanned_books'] += scanned
    signup_period -= 1

used_libs = [libs[i] for i in lib_signup]
print(used_libs)

def generateOutput(output_libs):
    global filename
    f = open(filename + '_sol.txt', 'w')
    f.write(str(len(output_libs))+ '\n')
    
    for out_lib in output_libs:
        f.write(str(out_lib['id']) + ' ' + str(len(out_lib['scanned_books'])) + '\n')
        out_books = "".join([str(b) + ' ' for b in out_lib['scanned_books']])[:-1]
        f.write(out_books + '\n')
    f.close()

generateOutput(used_libs)
