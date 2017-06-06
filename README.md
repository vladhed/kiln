# kiln
Raspbery Pi Zero W Kiln Controller

copyright 2017 Dominic Richens

Uses https://github.com/steve71/MAX31856 to read kiln temp from a K-type 
thermocouple.
GPIO through transistor to drive BEM-14840DA 40A SSR

Usage: kilncon.py -c <cone> -r <ramp> -s <soak>
	cone - 01 to 09 or 1 to 13 - default is 04 (1060 C)
	ramp - degrees C / hr - default is 200
	soak - time to hold at 100 C - default 2 hrs

cgi-bin/temp.py is a web page that displays the current temperature and
a chart of the temperature over time since kilncon was started.

plot.it is a gnuplot script for printing the chart.
