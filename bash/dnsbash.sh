#!/bin/bash

while read line; do
    for word in $line; do
        stripped=`echo $word |tr -cd '[:alnum:]'`
	dig +short +time=1 +retry=0 @10.0.10.200 $stripped'.google.ca'
    done
done <"data.txt"
