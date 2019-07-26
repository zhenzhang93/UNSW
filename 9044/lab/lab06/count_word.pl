#!/usr/bin/perl -w

if (@ARGV == 1 ){
	my $number = 0;
	while (my $line = <STDIN>){
		$line =~ s/^\s*//g;
		my @arr = split(/[^a-zA-Z]+/,$line);
		foreach my $word(@arr){
			my $w = lc($ARGV[0]);
			$number++ if lc($word) eq "$w";
		}
	}

	print "$ARGV[0] occurred $number times\n"

}

