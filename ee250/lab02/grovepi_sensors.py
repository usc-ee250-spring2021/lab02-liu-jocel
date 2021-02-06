

""" EE 250L Lab 02: GrovePi Sensors

List team members here.

Insert Github repository link here.
"""

"""python3 interpreters in Ubuntu (and other linux distros) will look in a 
default set of directories for modules when a program tries to `import` one. 
Examples of some default directories are (but not limited to):
  /usr/lib/python3.5
  /usr/local/lib/python3.5/dist-packages

The `sys` module, however, is a builtin that is written in and compiled in C for
performance. Because of this, you will not find this in the default directories.
"""
import sys
import time
from grove_rgb_lcd import * 
# By appending the folder of all the GrovePi libraries to the system path here,
# we are successfully `import grovepi`
sys.path.append('../../Software/Python/')
# This append is to support importing the LCD library.
sys.path.append('../../Software/Python/grove_rgb_lcd')

import grovepi

"""This if-statement checks if you are running this python file directly. That 
is, if you run `python3 grovepi_sensors.py` in terminal, this if-statement will 
be true"""
if __name__ == '__main__':

    setRGB(0,255,0)
    PORT = 4    # D4
    POT = 0	# A0

    while True:
        #So we do not poll the sensors too quickly which may introduce noise,
        #sleep for a reasonable time of 200ms between each iteration.
        time.sleep(0.2)
	threshold = grovepi.analogRead(POT)
	dist = grovepi.ultrasonicRead(PORT)

	if dist <= threshold:
	   l1 = str(threshold)+" cm OBJ PRES"
	   mask = " "
	   while len(l1+mask) < 16:
		mask += " "
	   setText_norefresh(l1+mask+"\n"+str(dist)+" cm")
	   setRGB(255,0,0)
	else:
	   l1 = str(threshold)+" cm"
	   mask = " "
	   while len(l1+mask) < 16:
		mask += " "
	   setText_norefresh(l1+mask+"\n"+str(dist)+" cm")
	   setRGB(0,255,0)
