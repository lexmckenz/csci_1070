#!/usr/bin/env python3
import sys

def mapper():
    """
    Reads in a sentences and maps the values.
    Mapping the values means it will give a
    count of 1 to every word in a sentence.

    Words are defined if there is a space
    between them.
    """

    #stdin = standard input
    for line in sys.stdin:
        #strip white space at the beginning
        # and end of the the line
        line = line.strip()

        #split the line into words
        words = line.split()
        
        #process each word and assign
        # a value of 1 to each word
        for word in words:
            print(word + "\t1")
            sys.stdout.flush() #might need this line on windows to show in console output

if __name__=="__main__":
    mapper()
