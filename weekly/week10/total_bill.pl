#!/usr/bin/perl -w

if(@ARGV == 1){
	
	open(F,'<',$ARGV[0]) or die;
	my $total = 0;
	foreach my $line(<F>){
		if($line =~ /"price": "\$(.*)"/){
			$total += $1;
		}
	}
	$res = sprintf "%.2f",$total;
	print "\$$res\n";

}
