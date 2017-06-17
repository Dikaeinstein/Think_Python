import random
import bisect 

import string

def process_line ( line, verbose=False ):
    '''
    Break line into words. Then strip whitespace and punctuations from words.
    
    line: line of text from file.
    verbose: boolean arg, True to print or False if not.
    '''
    hist = {}
    strippables = string.whitespace + string.punctuation
    line = line.replace("-", " ")
    
    for word in line.split():
        word = word.strip(strippables).lower()
        if verbose:
            print(word)
        hist[word] = hist.get(word, 0) + 1
    total = sum(hist.values())
    
    return hist, total


def process_file ( filename, skip_header=False ):
    fin = open(filename)
    word_count = 0
    word_hist = {}
    
    if skip_header:
        skip_gutenberg_header(fin)
        
    for line in fin:
        d, count = process_line(line)
        word_count += count
        for word, freq in d.items():
            if word not in word_hist:
                word_hist[word] = freq
            else:
                word_hist[word] += freq
                
    return word_hist, word_count
             

def skip_gutenberg_header(fp):
    """Reads from fp until it finds the line that ends the header.

    fp: open file object
    """
    for line in fp:
        if line.startswith('*END*THE SMALL PRINT!'):
            break


hist_map = {}
def choose_from_hist ( hist ):
    key = tuple(hist)
    if key not in hist_map:
        t = []
        for letter, freq in hist.items():
            t.extend([letter] * freq)      
        hist_map[key] = t
        return random.choice(t)   
    
    return random.choice(hist_map[key])
   

'''
cum_dict = {}
def choose_from_hist ( hist ):
    words = []
    total_freq = 0
    
    # build word and cumm frequency list
    for word, freq in hist.items():
        words.append(word)
        if freq not in cum_dict:
            total_freq += freq
            cum_dict[freq] = total_freq
           
    # generate a random value and find its location in cummulative list
    n = max(cum_dict.values())
    x = random.randint(1, n)
    cum_freqs = list(cum_dict.values())
    index = bisect.bisect_left(cum_freqs, x)
    
    return words[index]
'''    
    


def main():
    filename = "/storage/sdcard1/python/think_python/emma.txt"
    hist, total = process_file(filename, skip_header=True)

    print("\n\nHere are some random words from the book:\n")
    for i in range(500):
        print(choose_from_hist(hist), end=' ')


if __name__ == '__main__':
    main()