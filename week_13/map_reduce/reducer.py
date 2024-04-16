#!/usr/bin/env python3
import sys

def reduce_mapped():
    """
    Reduce mapped values
    """
    current_word = None
    current_count = 0

    #loop through lines passed in from 
    #mapper.py program
    for line in sys.stdin:
        line = line.strip()
        word, count = line.split("\t",1)

        count = int(count)

        if current_word == word:
            current_count += count

        else:
            #if there a current word
            #and its not none
            if current_word:
                print(current_word + "\t" + str(current_count))
            current_count = count
            current_word = word

    if current_word == word:
        print(current_word+ "\t"+str(current_count))

if __name__ == "__main__":
    reduce_mapped()

#echo 'the quick brown fox jumps over the lazy dog'|./mapper.py|sort|./reducer.py  