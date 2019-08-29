#!/bin/sh

for stu in `ls /import/ravel/2| grep -P 'z[0-9]{7}'`
do
	name=`acc $stu|egrep 'Name'|cut -d ':' -f2 |sed 's/Ali[^ ]* //g'| tr '\n' '   '`
	degree=`acc $stu|cut -d ':' -f2 | egrep '_Student' |tr ',' '\n'`
	position=`acc $stu | egrep 'Position'|cut -d':' -f2`
	echo "$name"
	echo "$position"
	echo "$degree"
	
	echo "----------------------------------"
done
