#!/usr/bin/python

import cgi
import max31856

csPin = 8
misoPin = 9
mosiPin = 10
clkPin = 11
max = max31856.max31856(csPin,misoPin,mosiPin,clkPin)
thermoTempC = max.readThermocoupleTemp()
thermoTempF = (thermoTempC * 9.0/5.0) + 32
thermoLimit = 2000

fs = cgi.FieldStorage()

for key in fs.keys():
  if key == "limit":
    thermoLimit = float(fs[key].value)

print "Content-type:text/html\r\n\r\n"
print '<html>'
print '<head>'
print '<meta http-equiv="refresh" content="5">'
print '<meta http-equiv="pragma" content="no-cache">'
print '<meta http-equiv="cache-control" content="max-age=0" />'
print '<meta http-equiv="cache-control" content="no-cache" />'
print '<meta http-equiv="expires" content="0" />'
print '<meta http-equiv="expires" content="Tue, 01 Jan 1980 1:00:00 GMT" />'
print '<title>Kiln Monitor</title>'
print '</head>'
print '<body>'
print '<h2>Temperature is %0.1f degC</h2>' % thermoTempC
print '<img src="output.png">'

if thermoTempC > thermoLimit:
  print '<audio autoplay="autoplay"><source src="ding.ogg" type="audio/ogg" /></audio>'
  print '<audio autoplay="autoplay"><source src="ding.mp3" type="audio/mp3" /></audio>'

print '</body>'
print '</html>'
