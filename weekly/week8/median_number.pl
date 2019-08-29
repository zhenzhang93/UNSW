#!/usr/bin/perl -w

my @arr = ();

if(@ARGV > 0){
	for(my $i = 0; $i < @ARGV; $i++){
		push @arr,$ARGV[$i];
	}
	
	my @sort_arr = sort {$a <=> $b}@arr;

	if(@ARGV % 2 == 0){
		my $res = $sort_arr[@ARGV/2] + $sort_arr[@ARGV/2-1];
		print $res,"\n";
	}
	else{
		my $res =$sort_arr[(@ARGV-1)/2];
		print $res,"\n";
	}
}
