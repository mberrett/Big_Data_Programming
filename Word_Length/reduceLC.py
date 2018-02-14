
#!/usr/bin/env python

from operator import itemgetter
import sys

current_length = None
current_count = 0
length = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapLC.py
    length, count = line.split('\t', 1)

    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:  # count was not a number
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: length) before it is passed to the reducer
    if current_length == length:
        current_count += count
    else:
        if (current_length != 0) & (current_length != None):
            # write result to STDOUT
            print('%s\t%s' % (current_length, current_count))
        current_count = count
        current_length = length

# do not forget to output the last length if needed!
if current_length == length:
    print('%s\t%s' % (current_length, current_count))
