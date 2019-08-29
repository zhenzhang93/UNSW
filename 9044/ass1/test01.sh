#!/bin/sh


if [ -d ".legit" ]
then
	rm -rf ".legit/"
fi

echo -e "\033[32m========Testing start: test for commit========\033[0m"

rm -f a
rm -f output sample difference

touch a
./legit-add a >> output 
./legit-init >> output 
./legit-add a >> output 
./legit-commit -m commita >> output 
./legit-commit -m aaa >> output 
echo hello > a
./legit-add a >> output 
./legit-commit -m "" >> output 
./legit-commit -m :o >> output 
./legit-commit -m again >> output 



echo "legit-add: error: no .legit directory containing legit repository exists" >>sample
echo "Initialized empty legit repository in .legit" >>sample
echo "Committed as commit 0" >>sample
echo "nothing to commit" >>sample
echo "usage: legit-commit [-a] -m commit-message" >>sample
echo "Committed as commit 1" >>sample
echo "nothing to commit" >>sample


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
rm -f a 


