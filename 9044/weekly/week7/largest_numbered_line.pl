#!/usr/bin/perl -w

my @numarr = ();
my $maxnum;
my @lines = ();

while(my $line = <STDIN>){
	push @lines, $line;
	my @number=();
	if (@number = $line  =~ m/(-?\d*\.?\d+)/g ){
		
		push @numarr,@number;
		
		foreach my $num(@numarr){
			if(! $maxnum){
				$maxnum = $num;
			}
			else{

				if($num > $maxnum){
					$maxnum = $num;
				}
			}
		}
	}
}
if($maxnum){
	foreach my $newline(@lines){
		if($newline =~ /$maxnum/){
			print $newline;
		}
	}
}



