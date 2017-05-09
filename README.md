# com-diag-astrolabe

COPYRIGHT

Copyright 2017 by the  Digital Aggregates Corporation, Arvada Colorado USA.

LICENSE

Licensed under the terms of the FSF GPL v2.

ABSTRACT

Astrolabe is an implementation of a stratum-1 NTP server on a Raspberry
Pi 3 using a Microsemi chip-scale atomic clock (CSAC) integrated onto
a Jackson Labs Technologies CSAC GPS-disciplined oscillator (CSAC
GPSDO). The software is a slightly modified version of my Hourglass
project, being similarly based on Eric Raymond's clockmaker script.

CONTACT

Chip Overclock  
<mailto:coverclock@diag.com>  
Digital Aggregates Corporation  
3440 Youngfield Street  
Suite 209  
Wheat Ridge CO 80033 USA  

BLOG

<http://coverclock.blogspot.com/2017/05/my-stratum-0-atomic-clock_9.html>

IMAGES

<https://www.flickr.com/photos/johnlsloan/albums/72157680973310391>

REFERENCES

<http://catb.org/gpsd/hacking.html>

<http://git.savannah.gnu.org/cgit/gpsd.git/tree/build.txt>

<https://en.wikipedia.org/wiki/NTP_server_misuse_and_abuse>

<https://docs.ntpsec.org/latest/ntp_conf.html>

<http://catb.org/gpsd/gpsd-time-service-howto.html>

<https://docs.ntpsec.org/latest/ntp_conf.html>

REPOSITORIES

<https://github.com/coverclock/com-diag-astrolabe>

<https://github.com/coverclock/com-diag-hourglass>

<https://www.ntpsec.org/white-papers/stratum-1-microserver-howto/clockmaker>

<git://git.savannah.nongnu.org/gpsd.git>

<https://gitlab.com/NTPsec/ntpsec.git>

NOTES

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

    screen /dev/ttyUSB0 115200 8n1
    SYSTem:LCD:CONTrast 0.4

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

    sudo /etc/init.d/timeservice stop
    screen /dev/gpsd0 115200 8n1
    sudo ppstest /dev/pps0
    gpsmon /dev/gpsd0

    sudo gpsd -N -D 3 -b /dev/gpsd0 /dev/pps0
