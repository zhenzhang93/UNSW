#!/usr/bin/perl -w

use strict;

	
my %total=();
my %frequency=();
foreach my $file(glob "lyrics/*.txt"){
	open(F,'<',$file) or die;
	
	my $totalnumber = 0;
	my %times = ();

	while (my $line = <F>){
		$line =~ s/^\s*//g;
		my @arr = split(/[^a-zA-Z]+/,$line);
		foreach my $word(@arr){
			if ($word =~ /[a-zA-Z]+/){
				$totalnumber ++;
			}			
			$word = lc($word);
			$times{$word} += 1;
		}
	}
	
	$file =~ s/[^\/]*\/(.*)\.txt/$1/;
	$file =~ s/_/ /g;
	my %wordtimes = ();
	close F;
	foreach my $key(keys %times){
		my $res = log(($times{$key}+1) / $totalnumber);

		$wordtimes{$key} = $res;
	}

	$frequency{$file} = \%wordtimes;
	$total{$file} = $totalnumber;

}
	



if (@ARGV >= 1 ){
	my $flag = 0;
	if ($ARGV[0] eq '-d'){
		$flag = 1;
		shift(@ARGV);
	}


#	foreach my $key(keys %wordhash){
#		print "$wordhash{$key}{\"death\"}\n";
#	}

	foreach my $song(@ARGV){

		my %finalres = ();
		open(F,'<',$song) or die;
		my @content = <F>;
		
		foreach my $line(@content){
			$line =~ s/^\s*//g;
			my @arr = split(/[^a-zA-Z]+/,$line);
			foreach my $word(@arr){
				if ($word =~ /[a-zA-Z]+/){

					foreach my $person(keys %frequency){
						$word = lc($word);
						if(exists $frequency{$person}{$word}){
							$finalres{$person} += $frequency{$person}{$word};
						}			
						else{
							$finalres{$person} += log(1 / $total{$person});

						}	
					}
				}
			}
		}
		close F;
		if($flag ==1){
			foreach my $key(reverse sort{$finalres{$a} <=> $finalres{$b}}keys %finalres){
				printf "$song: log_probability of %.1f for $key\n",$finalres{$key};
			}

		}
		foreach my $key(reverse sort{$finalres{$a} <=> $finalres{$b}} keys %finalres){

			printf "$song most resembles the work of $key (log-probability=%.1f)\n",$finalres{$key};
			last;
		}
	}	
}

