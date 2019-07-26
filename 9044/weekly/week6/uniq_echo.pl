#!/usr/bin/perl -w

if(@ARGV gt 0){
	

	my @arr = ();

	foreach my $line(@ARGV){
		
		my $flag = 0;
		for(my $i = 0; $i < @arr; $i++){
			if($arr[$i] eq $line){
				$flag=1;
			}
		}
		
		if($flag == 0){
			push @arr,$line;
			print "$line ";
		}		
			
	}
	print "\n";

	
	
}
