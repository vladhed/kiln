#! /usr/bin/python

import sys
import time
import random
import os
import max31856
from optparse import OptionParser
from datetime import datetime

keep = 0
curr = 0

parser = OptionParser()

parser.add_option('-l','--limit',dest="templimit", help="Max temperature",metavar="int")
parser.add_option('-f','--file',dest="filename", help="Output for data",metavar="file")
options,remainder = parser.parse_args()

print options.templimit
limit = int(options.templimit)
print("shutoff at %d" % limit)

csPin = 8
misoPin = 9
mosiPin = 10
clkPin = 11
max = max31856.max31856(csPin,misoPin,mosiPin,clkPin)

file = options.filename
fo = open(file,"a",0)

last1=0
last2=0

while curr < limit:
    curr = max.readThermocoupleTemp()

    if last1 == 0:
      slope = (curr - last2)*120
    else:
      slope = (curr - last1)*60
    if slope > 1000:
      slope=100
    timestr = datetime.now().strftime("%H:%M:%S")
    print timestr+" "+str(curr)+" "+str(slope)
    fo.write(timestr+" "+str(curr)+"\n")
    cmd = "gnuplot -e \"set title 'C/hr = " + str(slope) + "';call 'plot.it2' \""
    os.system(cmd)

    last1 = last2
    last2 = curr
    time.sleep(30)
    if curr >= limit:
        print "Whaaaa?"

fo.close()
