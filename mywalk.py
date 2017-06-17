from os import walk, path

def directory(dirname, verbose=False):
    """Walks a given directory recursively.
    
    Returns a list of files.
    
    dirname: directory name.
    """
    res = []
    files = walk(dirname)
    for d, f, paths in files:
        for p in paths:
            if verbose:
                print(path.join(d, p))
            res.append(path.join(d, p))
            
    return res
        


'''       
import os
def walk ( dirname ):
    filenames = os.listdir(dirname)
    for name in filenames:
        filename = os.path.join(dirname, name)
        if os.path.isfile(filename):
            print(filename)
        else:
            walk(filename)
'''

if __name__ == "__main__":
    
    d = "/storage/sdcard1/python/think_python"
    directory(d, True)