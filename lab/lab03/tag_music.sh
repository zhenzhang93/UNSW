#!/bin/sh


for file in "$@"

do

		Album=`echo $file |cut -d '/' -f2`
		Year=`echo $file |cut -d '/' -f2 | cut -d ',' -f2 |sed 's/ //g'`
		echo "$Year ++++++ $Album"
		
		cd "$file"
		for f in *
		do
			newfile=`echo "$f" | sed 's/ - /+/g'`
			
			Title=`echo "$newfile"|cut -d '+' -f2| sed 's/^ //g'`	
			Artist=`echo "$newfile"|cut -d '+' -f3|sed 's/.mp3//' |sed 's/^ //g'`	
			Track=`echo "$newfile" | cut -d '+' -f1 | sed 's/^ //g'` 

			
			id3  "$f" -a  "$Artist"  >/dev/null
			id3  "$f" -t  "$Title"  >/dev/null
			id3  "$f" -T  "$Track"  >/dev/null
			id3  "$f" -y	"$Year" >/dev/null
			id3  "$f" -A  "$Album"  > /dev/null
			
		done	
		cd ../
		cd ../
		

done

