#!/bin/dash

number=0

while [ -d .snapshot.$number ]
do

	number=`expr $number + 1`
done

mkdir .snapshot.$number
path=.snapshot.$number

filenames=`ls | egrep -v 'snapshot-(save|load).sh'`

for file in $filenames
do
	cp $file $path
done

echo "Creating snapshot $number"
