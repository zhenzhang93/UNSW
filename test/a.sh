#!/bin/sh

echo '$0' is $0

echo '$1' is $1

echo '$2' is $2
echo '$3' is $3

echo all my arguement are $@


echo all my arguement is the number $#

echo the process $?

i=10

i=`expr $i + 1`
echo "by expr i+1, i is $i"

((i++))

echo "by (()) i+1, i is $i"

let i+=1


echo "by let i+=1, i is $i"

i=$[$i+1]

echo "by \$[\$i+1], i is $i"









myfuc() {
	echo $1 $2
	return 5
}

myfuc "hello " "world"
echo $?














