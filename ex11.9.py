from os import chdir
from math import log
chdir("/storage/sdcard1/python/think_python/")
from proc import process_file


def rank_freq ( filename ):
    words_hist, total = process_file(filename, True)
    t = []
    freqs = sorted(words_hist.values())
    freqs.sort(reverse=True)
       
    for rank, freq in enumerate(freqs):
        r = rank+1
        t.append((r, freq))
    
    return t



def print_ranks ( t, n=100 ): 
    count = 0 
    for rank, freq in t:
        if count > n:
            break
        log_freq = log(freq)
        log_rank = log(rank)      
        print(rank, freq, log_freq, log_rank, sep="\t")
        count += 1
        


filename = "/storage/sdcard1/python/think_python/emma.txt"    
print("rank\tfrequency\tlogf\tlogr")
print_ranks(rank_freq(filename))