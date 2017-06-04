# com-diag-astrolabe

## Copyright

Copyright 2017 by the  Digital Aggregates Corporation, Arvada Colorado USA.

## License

Licensed under the terms of the FSF GPL v2.

## Abstract

Astrolabe is an implementation of a stratum-1 NTP server on a Raspberry
Pi 3 using a Microsemi chip-scale atomic clock (CSAC) integrated onto a
Jackson Labs Technologies (JLT) CSAC GPS-disciplined oscillator (CSAC
GPSDO). The software is a slightly modified version of my Hourglass
project, being similarly based on Eric Raymond's clockmaker script.

## Contact

Chip Overclock  
<mailto:coverclock@diag.com>  
Digital Aggregates Corporation  
3440 Youngfield Street  
Suite 209  
Wheat Ridge CO 80033 USA

## Trademarks

Chip Overclock is a registered trademark of John Sloan.

Digital Aggregates Corporation is a registered trademark of the Digital
Aggregates Corporation.

## Blog

<http://coverclock.blogspot.com/2017/05/my-stratum-0-atomic-clock_9.html>

## Images

<https://www.flickr.com/photos/johnlsloan/albums/72157680973310391>

## References

<http://catb.org/gpsd/hacking.html>

<http://git.savannah.gnu.org/cgit/gpsd.git/tree/build.txt>

<https://en.wikipedia.org/wiki/NTP_server_misuse_and_abuse>

<https://docs.ntpsec.org/latest/ntp_conf.html>

<http://catb.org/gpsd/gpsd-time-service-howto.html>

<https://docs.ntpsec.org/latest/ntp_conf.html>

<http://www.jackson-labs.com/assets/uploads/main/CSAC_Manual_v1_6.pdf>

## Repositories

<https://github.com/coverclock/com-diag-astrolabe>

<https://github.com/coverclock/com-diag-hourglass>

<https://www.ntpsec.org/white-papers/stratum-1-microserver-howto/clockmaker>

<git://git.savannah.nongnu.org/gpsd.git>

<https://gitlab.com/NTPsec/ntpsec.git>

## Remarks

If you power the JLT GPSDO board via USB to the Raspberry Pi 3 like I did,
the the ARM microcontroller on the GPSDO enumerates a serial port. You
can ssh into the PI and from there screen into the USB serial port to
get an SCPI command shell. This is exactly the same command shell that
is available via the external RS232 connection that I wired up (you can
use both at the same time).

    screen /dev/ttyUSB0 115200 8n1

You only have to issue the setup commands through this interface (or
the RS232 interface) once ever; the settings are saved in NVRAM.

You'll panic the first time you try to connect the LCD display to the
ARM microcontroller on the JLT GPSDO board and nothing shows up. That's
because the default contrast for the display, set using a software
command, isn't useful. Here's what worked for me.

    SYSTem:LCD:CONTrast 0.4

Astrolabe (a.k.a. "O-2") originally used the raw u-Blox GPS NMEA stream
to feed the GPS daemon. After some discussion with the kind folks at JLT
who make the CSAC GPSDO, I swapped the serial cables around to feed the
GPS daemon from the ARM microcontroller on the GPSDO. This is supposed to
work better (or: at all) during holdever when the GPS lock is lost. To get
the ARM to output the NMEA sentences to its console serial port requires
the following commands (again, which only need to be done once, ever).

    GPS:PORT RS232
    GPS:GPGGA 1
    GPS:GPRMC 1
    GPS:GPZDA 1
    GPS:GPGSV 1

If like me you are using Eric Raymond's clockmaker script, you will
be building the GPS daemon (gpsd) and NTP daemon (ntpd) right on the
Raspberry Pi.  But to duplicate my project, you'll want to re-build
and re-install the GPS daemon with some custom parameters. Here are
the commands to do that.  You'll also want to run the GPS daemon in
"broken" mode so it doesn't try to talk to the GPS device, because
it isn't... it's talking to the SCPI command interface on the ARM
microcontroller, which we configured above to deliver NMEA via that
same interface to the GPS daemon. I've already specified the "-b" flag
in the /etc/init.d/timeservice script in the overlay directory.

    cd src/clockmaker/gpsd
    scons --clean
    scons \
    	fixed_port_speed=115200 \
    	fixed_stop_bits=1 \
    	gpsdclients=yes \
    	magic_hat=yes \
    	ncurses=yes \
    	nmea0183=yes \
    	ntp=yes \
    	ntpshm=yes \
    	oscillator=yes \
    	pps=yes \
    	prefix="/usr/local" \
    	reconfigure=no \
    	shared=no \
    	socket_export=yes \
    	timeservice=yes
    scons
    scons install

Use these commands to stop, start, or restart the time service (gpsd
and ntpd) on the Pi.

    sudo /etc/init.d/timeservice stop
    sudo /etc/init.d/timeservice start
    sudo /etc/init.d/timeservice restart

Use this command on the Pi to connect to the SCPI USB serial interface
on the ARM microcontroller.

    screen /dev/gpsd0 115200 8n1

Run this command to test the 1PPS after stopping the time service.

    sudo ppstest /dev/pps0

Run this command to test the NMEA stream after stopping the time service.

    gpsmon /dev/gpsd0

## Notes

    Apr 25 11:36:16 mercury kernel: [959158.661259] usb 1-4.4: new full-speed USB device number 13 using xhci_hcd
    Apr 25 11:36:16 mercury kernel: [959158.768366] usb 1-4.4: New USB device found, idVendor=0403, idProduct=6001
    Apr 25 11:36:16 mercury kernel: [959158.768374] usb 1-4.4: New USB device strings: Mfr=1, Product=2, SerialNumber=3
    Apr 25 11:36:16 mercury kernel: [959158.768379] usb 1-4.4: Product: FT232R USB UART
    Apr 25 11:36:16 mercury kernel: [959158.768383] usb 1-4.4: Manufacturer: FTDI
    Apr 25 11:36:16 mercury kernel: [959158.768387] usb 1-4.4: SerialNumber: A504A2OG
    Apr 25 11:36:16 mercury kernel: [959158.771690] ftdi_sio 1-4.4:1.0: FTDI USB Serial Device converter detected
    Apr 25 11:36:16 mercury kernel: [959158.771758] usb 1-4.4: Detected FT232RL
    Apr 25 11:36:16 mercury kernel: [959158.772216] usb 1-4.4: FTDI USB Serial Device converter now attached to ttyUSB1
    Apr 25 11:35:40 mercury wpa_supplicant[1194]: message repeated 17 times: [ wlan0: Failed to initiate sched scan]
    Apr 25 11:36:16 mercury mtp-probe: checking bus 1, device 13: "/sys/devices/pci0000:00/0000:00:14.0/usb1/1-4/1-4.4"
    Apr 25 11:36:16 mercury mtp-probe: bus: 1, device: 13 was not an MTP device

    cd src/clockmaker/gpsd
    scons --help
    scons --clean
    scons \
    	fixed_port_speed=38400 \
    	fixed_stop_bits=1 \
    	gpsdclients=yes \
    	magic_hat=yes \
    	ncurses=yes \
    	nmea0183=yes \
    	ntp=yes \
    	ntpshm=yes \
    	oscillator=yes \
    	pps=yes \
    	prefix="/usr/local" \
    	reconfigure=no \
    	shared=no \
    	socket_export=yes \
    	timeservice=yes \
    	ublox=yes
    scons
    scons install

    sudo gpsd -N -D 3 -b /dev/gpsd0 /dev/pps0
