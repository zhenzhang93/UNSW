#!/usr/bin/perl -w

if (@ARGV eq 1){
	open(F,'<',$ARGV[0]) or die;
	my @arr=();
	while(my $line = <F>){
		$line =~ s/[0-9]/#/g;
		push @arr,$line;

	}
	close F;
	
	open(F,'>',$ARGV[0]) or die;
	
	foreach my $line(@arr){
		print F $line;
	}
	close F;


}
