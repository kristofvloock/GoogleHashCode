from math import log

def lib_score(D, day, libs, avg_scores):
    library_scores = []
    for i,l in enumerate(libs):
        p_occupied = l['scan_days']/(D - day)
        work_performed = l['nob']/max(p_occupied,1)
        library_scores.append(work_performed*avg_scores[i]/log(l['sup']))
    return library_scores

def avg_score(libs,book_scores):
    avg_scores = []
    for l in libs:
        books = l['books']
        avg_scores.append(sum([book_scores[i] for i in books])/l['nob'])
    return avg_scores
