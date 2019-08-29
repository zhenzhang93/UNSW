#!/bin/sh


#test-case6
IFS=$'\n'

if [ $# -eq 2 ]
then
	if [ -d $1 ]
	then
		for file in `ls $1|sort`	
		do

		
			
			filebasename=`basename "$file"`
			#filebasename=`echo $file|sed -r "s/$1\/(.*)/\1/"`
			
			if [[ -e "$2/$filebasename" ]]
			then
					
				
				
				diff "$1/$file" "$2/$filebasename" > /dev/null 2>&1
				if [ $? -eq 0 ]
				then
					echo "$filebasename"
					
				fi
		
			fi

		done
	fi
fi
