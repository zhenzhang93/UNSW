#!/usr/bin/perl -w

while(my $line = <STDIN>){
	my @arr = split(/\s+/,$line);
	print join(' ',sort @arr),"\n";

}
