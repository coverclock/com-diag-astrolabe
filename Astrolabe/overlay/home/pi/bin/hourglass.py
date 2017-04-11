#!/usr/bin/python
# Copyright 2017 Digital Aggregates Corporation, Arvada Colorado USA.
# Licensed under the terms of the GPL v2.

import subprocess
import time
import Adafruit_CharLCD as LCD

lcd = LCD.Adafruit_CharLCDPlate()

lcd.enable_display(True)
lcd.show_cursor(False)
lcd.clear()

was = time.strftime("%a %Y-%b-%d\n %H:%M:%S %Z")
while True:
	if lcd.is_pressed(LCD.SELECT):
		lcd.set_cursor(0, 0)
		lcd.clear()
		lcd.message("    RTC")
		status = subprocess.call(["/sbin/hwclock", "-u", "-w"])
		lcd.set_cursor(0, 0)
		lcd.clear()
		if (status == 0):
			lcd.message("    RTC\n    Okay")
		else:
			lcd.message("    RTC\n    Fail")
		time.sleep(0.5)
		while lcd.is_pressed(LCD.SELECT):
			continue
		lcd.clear()
	now = time.strftime("%a %Y-%b-%d\n %H:%M:%S %Z")
	if was != now:
		lcd.set_cursor(0, 0)
		lcd.message(now)
		#print now
		was = now
	time.sleep(0.2)
