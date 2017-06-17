import shelve
from contextlib import closing
import cwd
from anagram_sets import signature, all_anagrams

def store_anagrams(filename, anagram_map):
    '''Stores anagram from a dictionary in a shelf.
    
    filename: string filename of shelf.
    anagram_map: mapping from sorted word to list of its anagram.
    '''
    with closing(shelve.open(filename, "c")) as shelf:  
        for word, word_list in anagram_map.items():
            shelf[word] = word_list
    
               
def read_anagrams(word, filename):
    '''Reads database and returns list of angrams for given word.
    
    word: string word to lookup.
    filename: string filename of shelf.
    '''
    with closing(shelve.open(filename)) as shelf:
        sig = signature(word)
        try:
            return shelf[sig] 
        except KeyError:
            return []     


if __name__ == "__main__":
    #d = all_anagrams("words.txt")  
    #store_anagrams("anagramdb", d)
    print(read_anagrams("opts", "anagramdb"))