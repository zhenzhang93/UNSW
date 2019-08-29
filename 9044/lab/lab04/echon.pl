#!/usr/bin/perl -w

my $number = $#ARGV;


if($number != 1){
	printf "Usage: $0 <number of lines> <string>\n"
}

elsif($ARGV[0] !~ /^[0-9]*$/){
	printf "./echon.pl: argument 1 must be a non-negative integer\n"
}

else{
	while ($ARGV[0]>0){
		printf "$ARGV[1]\n";
		$ARGV[0]--;
	}
}





