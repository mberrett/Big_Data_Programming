#!/usr/bin/env python

from operator import itemgetter
import sys

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into day, tmax and tmin
    day, tmax, tmin = line.split()

        # if tmin is below 10 OR tmax is above 40 and it is not a missing value (coded as -9999)
    if (float(tmin) < 10) & ((float(tmax) != -9999) | (float(tmin) != -9999)):
        # print results
        print('%s\t%s' % (day, "cold day"))
    elif (float(tmax) > 40) & ((float(tmax) != -9999) | (float(tmin) != -9999)):
        # print results
        print('%s\t%s' % (day, "hot day"))
