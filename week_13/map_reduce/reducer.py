#!/usr/bin/env python3
import sys

def reduce_mapped():
    """
    Reduce the mapped values. 

    In short, it will add up the ones for
    words that are the same.
    """
    current_word = None
    current_count = 0
    
    #loop thorugh the lines passed in from
    #mapper.py program
    for line in sys.stdin:
        line = line.strip()
        word, count = line.split("\t",1)

        count = int(count)

        if current_word == word:
            current_count += count
        
        else:
            # if there is a current word
            # that is not none and its not
            # the same as the word we're
            # currently on in our iterations
            if current_word:
                print(current_word + "\t" + str(current_count))

            current_count = count
            current_word = word
        
    if current_word == word:
        print(current_word + "\t" + str(current_count))

if __name__ == "__main__":
    reduce_mapped()