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


def most_freq ( words_hist ):
    '''
    Print 20 most frequebtly used words in dict.
    
    words_dict: dictionary with words as keys.
    '''
    t = []
    count = 0
    for word, freq in words_hist.items():
        t.append((freq, word))
    t.sort(reverse=True)
    
    for freq, word in t:
        if count == 20:
            break
        print(word, freq, sep="\t")
        count += 1
        

def subtract ( d1, d2 ):
    '''Find words in dict(d1) that is not in dict(d2).
    
    d1: dict
    d2: dict
    
    returns: a new set of words, which is the diff between the sets.
    '''
    s1 = set(d1)
    s2 = set(d2)
    return s1.difference(s2)


def words_dict ():
    fin = open("/storage/sdcard1/python/think_python/words.txt", "r+")
    words = {}
    for word in fin:
        word = word.strip().lower()
        words[word] = None
    fin.close()
    return words


if __name__ == '__main__':
    filename = "/storage/sdcard1/python/think_python/emma.txt"
    words = words_dict()
    word_hist, total = process_file(filename, True)
    most_freq(word_hist)
    s = subtract(word_hist, words)
    for val in s:
        print(val)
    print(total)
