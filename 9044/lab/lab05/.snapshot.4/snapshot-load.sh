#!/bin/dash



if [ $# -eq 1 ]
then
	if [ -d .snapshot.$1 ]
	then

		snapshot-save.sh
		for file in .snapshot.$1/*
		do
			cp $file .
		done
		echo "Restoring snapshot $1"
	fi

fi
