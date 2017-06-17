import cwd

def sed(pattern, repl, src, dest):
    '''Reads from source file and writes to destination file.
    
    Replacing every occurence of pattern string with replacement string, in each line.
    
    pattern: old pattern string to match.
    repl: new replacement string.
    src: source file path.
    dst: destination file path.
    '''   
    with open(src, "r") as fin1, open(dest, "w") as fin2:
        for line in fin1:
            line2 = line.replace(pattern, repl)
            fin2.write(line2)
            

def main():           
    sed("ECMAScript", "JavaScript", "test.txt", "about.txt")
    # print contents of new written file 
    with open("about.txt") as fin:
        for line in fin:
            print(line)


if __name__ == "__main__":   
    main()       
    

            