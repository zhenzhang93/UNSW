#!/bin/sh


if [ $# -gt 2 ]
then 
	echo "Usage: ./echon.sh <number of lines> <string>"
	exit 2
elif [ $# -lt 2 ]
then
	echo "Usage: ./echon.sh <number of lines> <string>"
	exit 2
elif egrep -q '[^0-9]+' <<< "$1"
then
	echo "./echon.sh: argument 1 must be a non-negative integer"
	exit 2
elif [ $1 -gt -1 ]
then
	number=$1
	while [ $number -gt 0 ] 
	do
		echo $2
       		let 'number-=1'
	done
else
	echo "./echon.sh: argument 1 must be a non-negative integer"
	exit 2
fi
