#!/bin/sh

for file in $@
do
	text=`ls -l "$file"|cut -d ' ' -f6,7,8`
	convert -gravity south -pointsize 36 -draw "text 0,10 '$text'" "$file" temporary_file.jpg

	rm $file
	mv temporary_file.jpg "$file"

done
