#!/usr/bin/perl -w


if(@ARGV == 2){
  	my $res = 0;
	open(F,'<',$ARGV[1]) or die "can not open";
	foreach my $line (<F>){
	
		if($line =~ /"how_many": (.*),/){
			$num = $1;
			
		}
		my $name = "";
		if($line =~ /"species": "(.*)"/){
			$name = $1;
			
		}
		
		if($name eq $ARGV[0]){
			
			$res += $num; 
			$num = 0;
		}
	
	}




	print $res,"\n";
}
