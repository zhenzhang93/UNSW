#!/bin/sh

if [ $1 ]
then
	egrep 'COMP[2|9]041' "$1" |cut -d '|' -f3 |cut -d ',' -f2|cut -d ' ' -f2|sort|uniq -c|sort -r|head -1 | awk '{print $2}'

fi
