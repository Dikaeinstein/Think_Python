import cwd
from os import walk, path, getcwd, popen

def search(suffix, dirname=getcwd()):
    '''Search directory and sub-directory for files with given suffix.
    
    suffix: file extension string.
    dirname: directory path string.
    '''
    names = []
    files = walk(dirname)
    for d, f, filenames in files:
        for filename in filenames:
            if filename.endswith(suffix):
                names.append(path.join(d, filename))     
    names.sort()
    
    return names    


def pipe(cmd):
    '''Pipes command through to OS shell using pipe object.
    
    cmd: command string.
    '''
    fp = popen(cmd)  
    res = fp.read()
    fp.close()
   
    return res  


def compute_checksum(filename):
    '''Compute checksum of file using md5sum.
    
    filename: filepath string.
    '''
    return pipe("md5sum " + filename)  


def check_diff(name1, name2):
    '''Check diffence between two text files.
    
    Using the UNIX 'diff' command.
    
    name1: filepath string.
    name2: filepath string.
    '''
    cmd = "diff {0} {1}".format(name1, name2)
    
    return pipe(cmd)



def find_duplicates(suffix, dirname=getcwd()):
    '''Find duplicate files in directory.
    
    Using their checksum to find duplicates.
    suffix: file extension string.
    dirname: directory path string.
    '''
    duplicates = []
    files = search(suffix, dirname)  
    i = 0   
    
    while i < len(files)-1:  
        checksum = compute_checksum(files[i])
        checksum2 = compute_checksum(files[i+1])
        if checksum[:32] == checksum2[:32] and check_diff(files[i], files[i+1]) == "":
            duplicates.append((files[i], files[i+1]))
        i += 1
    
    return duplicates
        
    
def main():
    for f1, f2 in find_duplicates(".txt"):
        print(f1, f2)


if __name__ == "__main__":
    main()  