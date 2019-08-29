#!/bin/sh


if [ -d ".legit" ]
then
	rm -rf ".legit/"
fi

echo -e "\033[32m========Testing start: test for show and rm========\033[0m"

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
./legit-show 0:a >> output
./legit-show 1:a >> output
./legit-show 2:a >> output
./legit-show 0:b >> output
./legit-show 1:b >> output
./legit-show 2:e >> output
./legit-show 3:c >> output
./legit-show 4:c >> output
./legit-show :c >> output
echo c >> c
./legit-add c >> output 
./legit-commit -m c >> output
./legit-show :c >> output
rm a
./legit-add a >> output
./legit-commit delete-a >> output
./legit-log >> output
./legit-show :a >> output
./legit-show 4:c >> output
./legit-show :c >> output

./legit-rm --cached c >> output
./legit-show :c >> output

./legit-commit -m delete-a >> output
./legit-log >> output
./legit-show :a >> output
./legit-show 4:c >> output
./legit-show :c >> output
#delete c again
./legit-rm --cached c >>output
./legit-show :c >> output

	
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
echo "hello" >>sample
echo "hello" >>sample
echo "legit-show: error: 'b' not found in commit 0" >>sample 
echo "legit-show: error: 'b' not found in commit 1" >>sample 
echo "legit-show: error: 'e' not found in commit 2" >>sample 
echo "legit-show: error: unknown commit '4'" >>sample
echo "Committed as commit 4" >> sample
echo "c" >> sample
echo "usage: legit-commit [-a] -m commit-message" >> sample
echo "4 c" >> sample
echo "3 bcde" >> sample
echo "2 bcd" >> sample
echo "1 :o" >> sample
echo "0 a" >> sample
echo "legit-show: error: 'a' not found in index" >> sample
echo "c" >> sample
echo "c" >> sample
echo "legit-show: error: 'c' not found in index" >> sample

echo "Committed as commit 5">> sample
echo "5 delete-a" >> sample
echo "4 c" >> sample
echo "3 bcde" >> sample
echo "2 bcd" >> sample
echo "1 :o" >> sample
echo "0 a" >> sample
echo "legit-show: error: 'a' not found in index" >> sample
echo "c" >> sample
echo "legit-show: error: 'c' not found in index" >> sample
echo "legit-rm: error: 'c' is not in the legit repository" >> sample
echo "legit-show: error: 'c' not found in index" >> sample







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


