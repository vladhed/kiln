#! /usr/bin/python

import sys
import time
import random
import os
import max31856
from max31856 import FaultError
from optparse import OptionParser
from datetime import datetime

temphistory = [1, 0, 0, 0, 0]
secshistory = [1, 0, 0, 0, 0]

# averaging slope function
def slopecalc(newtemp,secs):
  global temphistory
  global secshistory

  #initial conditions
  i = 4
  while temphistory[i] == 0: 
    i=i-1

  if temphistory[i] != 1:
    slope = (newtemp - temphistory[i])*(3600/(secs-secshistory[i]))

    # shift values
    for i in range(0,3):
      temphistory[4-i]=temphistory[3-i]
      secshistory[4-i]=secshistory[3-i]
  else:
    # first call, make up a value
    slope = 100

  temphistory[0] = newtemp
  secshistory[0] = secs

  return slope


if __name__ == "__main__":

  curr = 0

  parser = OptionParser()

  parser.add_option('-l','--limit',dest="templimit", help="Max temperature",metavar="int")
  #parser.add_option('-f','--file',dest="filename", help="Output for data",metavar="file")
  options,remainder = parser.parse_args()

  print options.templimit
  limit = int(options.templimit)
  print("shutoff at %d" % limit)

  csPin = 8
  misoPin = 9
  mosiPin = 10
  clkPin = 11
  max = max31856.max31856(csPin,misoPin,mosiPin,clkPin)

  #file = options.filename
  file = "/var/www/html/temps"
  fo = open(file,"a",0)

  while curr < limit:
    try:
      curr = max.readThermocoupleTemp()
      secs = time.time()

      slope = slopecalc(curr,secs)
      timestr = datetime.now().strftime("%H:%M:%S")
      print timestr+" "+str(curr)+" "+str(slope)
      fo.write(timestr+" "+str(curr)+"\n")
      cmd = "gnuplot -e \"set title 'C/hr = " + str(slope) + "';call 'plot.it2' \""
      os.system(cmd)
    except FaultError as fault:
      print fault
      
    time.sleep(30)

  fo.close()
