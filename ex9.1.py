'''
reads words.txt and loops through it and prints 
only words with than 20 characters(not counting whitespace)
'''
words = open("/storage/sdcard1/python/think_python/test.txt", "r")

for word in words:
    if len(word.strip()) > 20:
        print(word)

