#!/usr/bin/python

import max31856
csPin = 8
misoPin = 9
mosiPin = 10
clkPin = 11
max = max31856.max31856(csPin,misoPin,mosiPin,clkPin)
thermoTempC = max.readThermocoupleTemp()
thermoTempF = (thermoTempC * 9.0/5.0) + 32

print "Content-type:text/html\r\n\r\n"
print '<html>'
print '<head>'
print '<meta http-equiv="refresh" content="5">'
print '<title>Hello Word - First CGI Program</title>'
print '</head>'
print '<body>'
print '<h2>Temperature is %0.1f degF</h2>' % thermoTempF
print '<img src="output.png">'
print '</body>'
print '</html>'
