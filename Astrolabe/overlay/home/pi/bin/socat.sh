#!/bin/bash
# Copyright 2017 Digital Aggregates Corporation, Arvada Colorado USA.
# Licensed under the terms of the GPL v2.

ONE=${1-"/dev/ttyUSB0"}
TWO=${2-"/dev/ttyUSB1"}
BPS=${3-"115200"}
exec socat file:${ONE},raw,b${BPS},cs8,echo=0 file:${TWO},raw,b${BPS},cs8,echo=0
