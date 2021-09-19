#!/bin/bash
SCRIPTLOC="/home/miklos_akos"
IPTABLES=$(which iptables)
GREP=$(which grep)
LSTFILE="/tmp/processed.lst"
$SCRIPTLOC/fuck-uceprotect.py || exit 255
while read ip; do iptables -n -L | $GREP $ip || $IPTABLES -A OUTPUT -d $ip -j DROP; done < ${LSTFILE}
