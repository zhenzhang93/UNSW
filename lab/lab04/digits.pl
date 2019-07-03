#!/usr/bin/perl -w

my @input=<STDIN>;
foreach my $line(@input){

	$line=~ s/[0-4]/</g;
	$line=~ s/[6-9]/>/g;
	printf $line;
}
