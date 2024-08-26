#!/usr/bin/python
# Copyright 2017-2024 Digital Aggregates Corporation, Arvada Colorado USA.
# Licensed under the terms of the GPL v2.

import subprocess
import time
import Adafruit_CharLCD as LCD

lcd = LCD.Adafruit_CharLCDPlate()

lcd.enable_display(True)
lcd.show_cursor(False)
lcd.clear()

fullstamp = "%a %Y-%b-%d\n %H:%M:%S %Z ?"
hourstamp = "%Y-%b-%d %H %Z"

was = time.strftime(fullstamp)
before = time.strftime(hourstamp)
while True:
	if lcd.is_pressed(LCD.SELECT):
		status = subprocess.call(["/sbin/hwclock", "-u", "-w"])
		if (status == 0):
			fullstamp = "%a %Y-%b-%d\n %H:%M:%S %Z ."
		else:
			fullstamp = "%a %Y-%b-%d\n %H:%M:%S %Z !"
		while lcd.is_pressed(LCD.SELECT):
			continue
	after = time.strftime(hourstamp)
	if before != after:
		status = subprocess.call(["/sbin/hwclock", "-u", "-w"])
		if (status == 0):
			fullstamp = "%a %Y-%b-%d\n %H:%M:%S %Z  "
		else:
			fullstamp = "%a %Y-%b-%d\n %H:%M:%S %Z !"
		before = after
	now = time.strftime(fullstamp)
	if was != now:
		lcd.set_cursor(0, 0)
		lcd.message(now)
		was = now
	time.sleep(0.2)
