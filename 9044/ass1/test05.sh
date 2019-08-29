#!/bin/sh


if [ -d ".legit" ]
then
	rm -rf ".legit/"
fi

echo -e "\033[32m========Testing start: test for rm========\033[0m"

rm -f a b c d e
rm -f output sample difference

touch a b c d e
./legit-add a >> output 
./legit-init >> output 
./legit-add a >> output 
./legit-commit -m a >> output 
./legit-commit -m aaa >> output 
./legit-add b c >> output
echo d >> d
echo e >> e
./legit-commit -m bc >> output 
./legit-rm --cached a >> output 
./legit-add e  >> output 
./legit-rm --cached e >> output 
./legit-rm e >> output 
./legit-rm a >> output 
./legit-rm --forced e >> output 
./legit-commit -m e >> output 
./legit-rm --force e >> output
./legit-show :e >> output

echo "legit-add: error: no .legit directory containing legit repository exists" >>sample
echo "Initialized empty legit repository in .legit" >>sample
echo "Committed as commit 0" >>sample
echo "nothing to commit" >>sample
echo "Committed as commit 1" >>sample
echo "legit-rm: error: 'e' is not in the legit repository" >>sample
echo "legit-rm: error: 'a' is not in the legit repository" >>sample
echo "legit-rm: error: invalid filename '--forced'" >>sample
echo "Committed as commit 2" >>sample
echo "legit-rm: error: 'e' is not in the legit repository" >>sample
echo "legit-show: error: 'e' not found in index" >>sample






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


