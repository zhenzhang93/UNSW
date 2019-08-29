#!/usr/bin/perl -w

my $number = 0;
while(my $line = <STDIN>){
	$line =~ s/^\s*//g;
	my @arr = split(/[^a-zA-Z]+/,$line);
	
#there may be empty string.
	foreach my $word(@arr){
		$number++ if $word =~ /[a-zA-Z]+/;
	}

	
	
	
}

print "$number words\n";
