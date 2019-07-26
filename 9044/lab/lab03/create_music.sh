#!/bin/sh

if [ $# -eq 2 ]
then
	wget -q -O- 'https://en.wikipedia.org/wiki/Triple_J_Hottest_100?action=raw' |
	while read line
	do
		if [[ "$line" =~ (Triple J Hottest 100, )+[0-9]{4} ]]
		then

			#echo $line
			
			content=`echo "$line" | sed -r 's/.*\[\[([^\|]*)\|.*/\1/g' `
			year=`echo $content| cut -d ',' -f2`
			directory="$2/Triple J Hottest 100, $year"
			mkdir -p -m 755 "$directory"	
		fi
		
		if [[ "$line" =~ ^#.* ]]
		then
			echo $line
		
		fi
		
	done

fi



