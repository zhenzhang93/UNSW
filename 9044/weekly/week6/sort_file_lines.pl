#!/usr/bin/perl -w

if (@ARGV == 1){
	open(F,'<',"$ARGV[0]") or die "can not open file\n";
	my %count = ();
	while(my $line = <F>){
		$count{$line} = length($line);
	}
	close F;
	

	foreach my $key (sort{ $count{$a} <=> $count{$b} or $a cmp $b } keys %count) {
		print "$key";
	}
	

}
