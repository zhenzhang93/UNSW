#!/bin/sh


if [ -d ".legit" ]
then
	rm -rf ".legit/"
fi

echo -e "\033[32m========Testing start: test for show,log========\033[0m"

rm -f a 
rm -f output sample difference

./legit-init >>output
echo line 2 >a
./legit-add a >> output
./legit-commit -a -m commit-0 >>output 
echo line 1 >>a
./legit-rm a >>output 
echo line 0 >>a
./legit-rm --cached a >>output 
./legit-commit -m commit-1 >>output 
./legit-rm --cached a >>output 
./legit-add a >>output 
./legit-commit -m commit-2 >>output 
cat "a" >>output
./legit-log >> output
./legit-show 2:a >> output
 


echo "Initialized empty legit repository in .legit" >>sample
echo "Committed as commit 0" >>sample
echo "legit-rm: error: 'a' in repository is different to working file" >>sample
echo "Committed as commit 1" >>sample
echo "legit-rm: error: 'a' is not in the legit repository" >>sample
echo "Committed as commit 2" >>sample
echo "line 2" >>sample
echo "line 1" >>sample
echo "line 0" >>sample
echo "2 commit-2" >>sample
echo "1 commit-1" >>sample
echo "0 commit-0" >>sample
echo "line 2" >>sample
echo "line 1" >>sample
echo "line 0" >>sample





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


