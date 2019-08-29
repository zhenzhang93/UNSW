#!/usr/bin/perl -w

open(F,'<',$ARGV[0]) or die;

my @content = <F>;

close F;

my $count = 0;

foreach(@content){
	
	$count++;
}


if($count %2==0){
	my $newcount = 0;
	foreach my $line(@content){
		$newcount++;
		if($newcount == $count/2 || $newcount == $count /2 +1){
			print $line;
		}
	}
}
else{
	my $newcount = 0;
	foreach my $line(@content){
		$newcount++;
		if($newcount == ($count+1)/2){
			print $line;
		}
	}
}
