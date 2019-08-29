#!/bin/sh


if [ -d ".legit" ]
then
	rm -rf ".legit/"
fi

echo -e "\033[32m========Testing start: test for branch========\033[0m"

rm -f a 
rm -f output sample difference

./legit-init >>output
echo line 2 >a
./legit-add a >> output
./legit-commit -a -m commit-0 >>output 
./legit-branch >>output 
./legit-branch b1 >>output 
./legit-branch b1 >>output 
./legit-branch 21 >>output 
./legit-branch c >>output 
./legit-branch >> output
 ./legit-branch b2 >>output 
 ./legit-branch b3 >>output
 ./legit-branch bb >>output  
./legit-branch >> output
./legit-branch -d s >> output
./legit-branch -d b1 b2 >> output
./legit-branch -d b1 >> output
./legit-branch -d bb >> output
./legit-branch >> output

echo "Initialized empty legit repository in .legit" >>sample
echo "Committed as commit 0" >>sample
echo "master" >>sample
echo "legit-branch: error: branch 'b1' already exists" >>sample
echo "legit-branch: error: invalid branch name '21'" >>sample
echo "b1" >>sample
echo "c" >>sample
echo "master" >>sample
echo "b1" >>sample
echo "b2" >>sample
echo "b3" >>sample
echo "bb" >>sample
echo "c" >>sample
echo "master" >>sample
echo "legit-branch: error: branch 's' does not exist" >>sample
echo "usage: legit-branch [-d] <branch>" >>sample
echo "Deleted branch 'b1'" >>sample
echo "Deleted branch 'bb'" >>sample
echo "b2" >>sample
echo "b3" >>sample
echo "c" >>sample
echo "master" >>sample



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

rm -f a 


