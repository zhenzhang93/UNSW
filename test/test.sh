#!/bin/sh

#while read line
#do
#	num=`echo $line|awk '{print $4}'`
#	bignum=`echo $num|awk -F':' '{print $1}'`
#	realnum=`expr $bignum + 12`
#	if (( $realnum >= 24 ))
#	then
#		realnum=$[realnum-12]
#		echo $realnum
#	fi
#done

# while read line
# do

# 	if [[ $line =~ (<(!.*)>) ]]
# 	then
# 		content=`echo "$line"|sed -r 's/<!(.*)>/\1/'`
# 		line=`echo $line|sed 's/<!.*>/<>/'`
# 		newcontent=`$content`
# 		newline=`echo $line|sed "s/<>/$newcontent/"`		
# 		echo $newline
# 	fi

# done

#while read line
#do
#	content=`echo $line|awk -F '|' '{print $3}'|cut -d ',' -f1`
	
#better use awk
#	ginvenname=`echo $line|cut -d '|' -f3 |cut -d ',' -f2`
	
	#a=ab
	#newres=`echo $line|sed "s/$a/cd/g"`

	
#	res=`echo $line|sed "s/$content,$ginvenname/$ginvenname $content/g"`
#	echo $res

#done



# tute week2  question2

# if [ $# == 1 ]
# then
# 	start=$1
# fi
# if [ $# == 2 ]
# then
# 	start=$1
# 	end=$2
# fi

# if [ $# == 3 ]
# then
# 	start=$1
# 	step=$2
# 	end=$3
# fi

# while (( $start<=$end ))
# do
# 	echo $start
# 	if [ $step ]
# 	then
# 		start=`expr $start + $step`
# 	else

# 		start=`expr $start + 1`	
# 	fi
# done





# tute week2  question3

# if [ $# -eq 0 ]
# then
# 	for file in *.bad
# 	do
# 		rm -rf $file
# 		echo "OK"
# 	done
# else
# 	for file in "$@"
# 	do
# 		if cat $file|egrep '< *blink *>' >/dev/null 
# 		then
# 			echo "rename them"
# 		fi	
# 	done

# fi



# tute week2  question4

# for file in *.c
# do
# 	echo "$file contains"

#	egrep '^#include' "$file"|  # find '#include lines
#    sed 's/[">][^">]*$//'|      # remove the last '"' or '>' and anything after it
#    sed 's/^.*["<]/    /'       # remove the first '"' or '>' and anything before it


# 	cat $file| while read line
# 	do
		#need to check there is include
# 		if [[ $line =~ \"(.*)\" ]]
# 		then
# 			content=`echo $line|sed -r 's/.*" *(.*) *".*/\1/'`
# 			echo "        "$content""
# 		fi

# 	done
# done


# tute week2  question8

# for file in "$@"
# do
# 	if [ ! -e $file ]
# 	then
# 		echo "NO such file $file"
# 		break
# 	fi
# 	name=`echo $file|sed s/\.gz//`
# 	echo "====$file===="
# 	cat $name
# done


# tute week2  question9



#sort $1 |join $2 -|cut -d ' ' -f2,4,5|sort -k2

#while read sid name givename hha gg
#do
#	echo $sid
#	echo $name
#	echo $givename
#	echo $hha
#	echo $gg
#done<g.txt



# tute week2  question10

# while read id mark
# do
# 	if echo $mark|egrep '^[0-9]+$' >/dev/null
# 	then
# 		if test $mark -gt 0 -a $mark -le 100
# 		then
# 			#use case or if
# 			case $mark in
# 			5[0-9]|6[0-9])
# 				echo "$id PS";;
# 			7[0-9]|8[0-9])
# 				echo "$id HD";;
# 			*)
# 				echo "FL";;
# 			esac
# 		else

# 			echo "$id ??"
# 		fi
# 	else
# 		echo "$id ??"
# 	fi

# done


#question 13

#for file in *
#do
#	content=`wc -c $file|awk '{print $1}'`
#	if (( $content >= 50 ))
#	then
#		echo "$file has $content"
#	fi
#done

#week3

#q5
#while read line
#do

#egrep -v ':'
#	if echo $line | egrep 'z[0-9]+'
#	then
#		echo $line
#	fi

#done

#wee3 q4

#hour=`date|cut -d ' ' -f4|cut -d ':' -f1`


#q9


# num=$1

# #for((i=2;i<=$num;i++))
# for i in $(seq 2 $num)
# do
# 	if (( $num % $i  == 0 ))
# 	then
# 		echo "buOK"
# 		exit 1
# 	fi
# done

# echo "OK"



#q7

# mlalias COMP2041-list|
# egrep -v :|
# sed 's/^ *//'|
# while read zid
# do
#     acc $zid|
#     cut -d: -f2|
#     tr , '\n'|
#     egrep _Student|
#     cut -c2-9|
#     egrep '[A-Z][A-Z][A-Z][A-Z][0-9][0-9][0-9][0-9]'
# done|
# sort|
# uniq -c|sort -rn

for i in $(seq 1 5)
do
	echo $i
done









