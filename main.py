# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

from itertools import count


def read_file_content(filename):
    # [assignment] Add your code here
    file_contents = open(filename, "r").read()
  
    return file_contents


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    words = text.lower().split()

    return {word:words.count(word) for word in words} 

