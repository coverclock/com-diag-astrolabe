#!/bin/bash
# Copyright 2017 Digital Aggregates Corporation, Arvada Colorado USA.
# Licensed under the terms of the FSF GPL v2.
# Compute the average offset for the GPS reference closk.
# <http://catb.org/gpsd/gpsd-time-service-howto.html>
# <https://docs.ntpsec.org/latest/ntp_conf.html>
FILE=${1-"/var/log/ntpstats/peerstats"}
cat ${FILE}.* | awk '
    BEGIN { tot0 = 0; num0 = 0; tot1 = 0; num1 = 0; }
    /127\.127\.28\.0/ { tot0 += $5; num0++; avg0 = tot0 / num0; print 0, $5, tot0, num0, avg0; }
    /127\.127\.28\.1/ { tot1 += $5; num1++; avg1 = tot1 / num1; print 1, $5, tot1, num1, avg1; }
    END { printf "%d %s %.7f\n", 0, "time1", 0 - avg0; printf "%d %s %.7f\n", 1, "time1", 0 - avg1; }
'
