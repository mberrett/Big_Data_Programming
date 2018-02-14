#!/usr/bin/env python

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split()
    # increase counters
    for word in words:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py

        # each words is a row of a tab delimited table
        day = words[1]  # 2nd column value
        tmax = words[5] # 6th column value
        tmin = words[6] # 7th column value

    print('%s\t%s\t%s' % (day, tmin, tmax))
