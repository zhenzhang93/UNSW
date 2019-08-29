#!/bin/sh


if [ $#>=1 ]
then
	
	for file in "$@"
	do
		
		content=`cat "$file" | egrep '\s*#\s*include\s*\".*\"' |sed -r 's/\s*#\s*include\s*\"(.*)\"/\1/'`
		
		for i in $content
		do 
			if [[ ! -f "$i" ]]
			then
				echo "$i included into $file does not exist"	
			fi
		done
		
	done

	

fi


