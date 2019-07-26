#!/bin/sh

for file in *
	
do
	
	suffix=`echo "$file"| sed -r 's/[^.]*.(.*)/\1/'`
	name=`echo "$file" | sed -r 's/([^.]*).(.*)/\1/'`
	string="htm"

	
	if [ "$suffix" == "$string" ]
	then	
		if [ -f "$name.html" ] 
		then
			echo "$name.html exists"
			exit 1

		else
				
			mv "$file" "$name.html"
		fi
	fi
	


done
	

