#!/bin/bash
# Compute the average offset for the GPS reference closk.
# <http://catb.org/gpsd/gpsd-time-service-howto.html>
# <https://docs.ntpsec.org/latest/ntp_conf.html>
FILE=${1-"/var/log/ntpstats/peerstats"}
exec awk '
     /127\.127\.28\.0/ { tot += $5; num++; avg = tot / num; print $5, tot, num, avg; }
     END { print "time1", 0 - avg; }
' < ${FILE}
