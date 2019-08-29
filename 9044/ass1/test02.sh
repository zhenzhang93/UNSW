#!/bin/sh


if [ -d ".legit" ]
then
	rm -rf ".legit/"
fi

echo -e "\033[32m========Testing start: test for log========\033[0m"

rm -f a b c d e
rm -f output sample difference

touch a b c d e
./legit-add a >> output 
./legit-init >> output 
./legit-add a >> output 
./legit-commit -m a >> output 
./legit-commit -m aaa >> output 
echo hello > a
./legit-add a >> output 
./legit-commit -m "" >> output 
./legit-commit -m :o >> output 
./legit-commit -m again >> output 
./legit-add b c d >> output 
./legit-commit -m bcd >> output 
./legit-log >> output
./legit-add b c d e >> output 
./legit-commit -m bcde >> output 
./legit-log >> output

	
echo "legit-add: error: no .legit directory containing legit repository exists" >>sample
echo "Initialized empty legit repository in .legit" >>sample
echo "Committed as commit 0" >>sample
echo "nothing to commit" >>sample
echo "usage: legit-commit [-a] -m commit-message" >>sample
echo "Committed as commit 1" >>sample
echo "nothing to commit" >>sample
echo "Committed as commit 2" >>sample
echo "2 bcd" >>sample
echo "1 :o" >>sample
echo "0 a" >>sample
echo "Committed as commit 3" >>sample
echo "3 bcde" >>sample
echo "2 bcd" >>sample
echo "1 :o" >>sample
echo "0 a" >>sample



diff -u "sample" "output" >difference

if [ $? == 1 ]
then
	echo -e "\033[31m'+' means your output unnessary  '-'means your output missing\033[0m"
    cat difference | sed -n '1,3!p'
    echo -e "\033[31mTest Failed\033[0m"
else
    echo -e "\033[32mTest Passed\033[0m"
fi



rm output sample difference 2> /dev/null

rm -rf ".legit/"

rm -f a b c d e


