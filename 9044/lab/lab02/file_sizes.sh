#!/bin/sh

small=""
medium=""
large=""
for FILE in *
do
	number=`cat $FILE|wc -l`
	#echo $number
	if [ -f $FILE ]
	then
		if [ $number -lt 10 ]
		then	
			small="$small $FILE" 
		elif [ $number -lt 100 ]
		then
			medium="$medium $FILE"
		else
			large="$large $FILE"
		fi  
	else
		echo "worng"
	fi	
done
echo "Small files: $small"
echo "Medium-sized files: $medium"
echo "Large files: $large"
