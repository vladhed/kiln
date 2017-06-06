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
fo = open(file,"w",0)

while curr < limit:
    curr = max.readThermocoupleTemp()
    currF = (curr * 9.0/5.0) + 32

    timestr = datetime.now().strftime("%H:%M:%S")
    print timestr+" "+str(currF)
    fo.write(timestr+" "+str(currF)+"\n")
    os.system("./plot.it")
    time.sleep(10)
    if curr >= limit:
        print "Whaaaa?"

fo.close()
