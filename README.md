# com-diag-astrolabe

COPYRIGHT

Copyright 2017 by the  Digital Aggregates CorporAation, Arvada Colorado USA.

LICENSE

Licensed under the terms of the FSF GPL v2.

ABSTRACT

NTP server based on Eric Raymond's clockmaker and the Jackson Labs CSAC GPSDO.

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
    GPS:PORT RS232
    GPS:GPGGA 1
    GPS:GPRMC 1
    GPS:GPZDA 1
    GPS:GPGSV 1
    GPS:PASHR 0

    cd clockmaker
    cd gpsd
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

    sudo /etc/init.d/timeservice stop
    screen /dev/gpsd0 115200 8n1
    sudo ppstest /dev/pps0
    gpsmon /dev/gpsd0

    sudo gpsd -N -D 3 -b /dev/gpsd0 /dev/pps0

REFERENCES

<http://catb.org/gpsd/hacking.html>

<http://git.savannah.gnu.org/cgit/gpsd.git/tree/build.txt>

<https://en.wikipedia.org/wiki/NTP_server_misuse_and_abuse>

<https://docs.ntpsec.org/latest/ntp_conf.html>
