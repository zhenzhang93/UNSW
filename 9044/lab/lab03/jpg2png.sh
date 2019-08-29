#!/bin/sh

for i in *.jpg

do
	filename=`sed -r 's/(.*).jpg/\1/' <<< $i`

	if [ -f "$filename.png" ]
	then
		echo "$filename.png already exists"	
	fi 
	
	if [ -f "$filename.jpg" ]
	then
		convert "$filename.jpg" "$filename.png"
		rm "$filename.jpg" 
	fi
done
