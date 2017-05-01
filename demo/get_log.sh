#!/bin/bash
LINENUM=$2
LOGFILE=$1
if [ $LINENUM ]; then
    sed -n ${LINENUM}p $LOGFILE
else
    wc -l $LOGFILE | awk '{print/$1}'
fi
