#!/bin/sh

echo '$0' is $0

echo '$1' is $1

echo '$2' is $2
echo '$3' is $3

echo by \$@ all my arguement are $@

echo by \$* all my arguement are $*


echo all my arguement is the number $#

echo the process $?

i=10

i=`expr $i + 1`
echo "by expr i+1, i is $i"

((i++))

echo "by ((i++)) i+1, i is $i"

let i+=1


echo "by let i+=1, i is $i"

i=$[$i+1]

echo "by \$[\$i+1], i is $i"


i=$(($i+1))

echo "by \$((\$i+1)), i is $i"


if test "$1" -ge 0 2>/dev/null
then
	echo "??"
# : Using : means do nothing  then :
#  	:
#if there is something not ineger, then print ok. then should exit
	
else
	echo "Ok"
fi 

i=$((i+1))
echo $i

for i in *
do
	ls -l "$i";


done | cat |awk '{print $9}'

#cheng fa 
i=$(expr $i \* $i)
echo $i



