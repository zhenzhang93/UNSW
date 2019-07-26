#!/usr/bin/perl -w

if (@ARGV == 1 ){
	foreach my $file(glob "lyrics/*.txt"){
		
		open(F,'<',$file) or die;
		my $number = 0;
		my $totalnumber = 0;
		while (my $line = <F>){
			$line =~ s/^\s*//g;
			my @arr = split(/[^a-zA-Z]+/,$line);
			foreach my $word(@arr){
				my $w = lc($ARGV[0]);
				$number++ if lc($word) eq "$w";
				$totalnumber++ if $word =~ /[a-zA-Z]+/;
			}
		}
		
		$file =~ s/[^\/]*\/(.*)\.txt/$1/;
		$file =~ s/_/ /g;
	
		close F;
		$res = log(($number+1) / $totalnumber);
		printf "log((%d+1)/%6d) = %8.4f %s\n",$number,$totalnumber,$res,$file;
	
	}

}

