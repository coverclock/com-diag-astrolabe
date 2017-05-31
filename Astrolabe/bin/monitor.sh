#!/bin/bash
SERVER=${1:-"astrolabe"}
DELAY=${2:-"30"}
while true; do date; ntpq -c peer -c as -c rl ${SERVER} ; sleep ${DELAY}; done
