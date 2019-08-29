#!/bin/sh


if [ -d ".legit" ]
then
	rm -rf ".legit/"
fi

rm -f output sample difference


echo -e "\033[32m========Testing start: test for init========\033[0m"

./legit-init >> output 
./legit-init >> output 


echo "Initialized empty legit repository in .legit" >>sample
echo "legit-init: error: .legit already exists" >>sample


diff -u "sample" "output" >difference

if [ $? == 1 ]
then
    cat difference
    echo -e "\033[31mTest Failed\033[0m"
else
    echo -e "\033[32mTest Passed\033[0m"
fi



rm output sample difference 2> /dev/null
rm -rf ".legit/"

