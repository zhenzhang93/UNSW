#!/bin/sh

if [ $# -eq 3 ]
then
	touch $3
	count=$1
	while [ $count -le $2 ]
	do
		echo $count >> $3
		((count++))
	done

fi
