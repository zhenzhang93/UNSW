#!/bin/sh

if [ $# >=1 ]
then
	
	for file in "$@"
	do
		echo "Address to e-mail this image to?"

		read email

		echo "Message to accompany image?"

		read message
	
		echo "$message" |mutt -s "penguins!" -e 'set copy=no' -a "$file" -- "$email"
		
		echo "$file sent to $email"

	done

fi