#!/usr/bin/perl -w


if(@ARGV == 1){
	my %arr = ();
	while(my $line = <STDIN>){
		
		$arr{$line} +=1;
		my $flag = 0;
		foreach my $key(keys %arr){
			
			if($arr{$key} == $ARGV[0]){
				print "Snap: $key";
				$flag = 1;
			}
		}
		if ($flag == 1){
			last;
		}
	
	
	}
}
