#!/bin/sh


if [ $# -eq 1 ]
then
	if [ -e $1 ]
	then

		if [ -f $1 ]
		then
			
			number=`ls -a | egrep "\.$1" |sed -r 's/.*\.([0-9]*)/\1/' |sort -nr|head -n1`
				
			if [ "$number" = "" ]
			then
				cp $1 .$1.0
				echo "Backup of '$1' saved as '.$1.0'"
			else
				number=$((number+1))
				cp "$1" ".$1.$number"
				echo "Backup of '$1' saved as '.$1.$number'"
			fi
								


			
		fi

	fi

fi
