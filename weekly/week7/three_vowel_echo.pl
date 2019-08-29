#!/usr/bin/perl -w

if(@ARGV >= 1){

	foreach my $word(@ARGV){
		my @arr = split(//,$word);
		my $num = 0;
		my $consecutiveflag = 0;
#last = 0 means last char is not vowel.

#it can also solved by /[aeiou]{3,}/i
		my $last = 0; 
		foreach my $char(@arr){
			if($last == 0){
				if($char =~ /[AEIOUaeiou]/){
					$last = 1;
					$num = 1;
				}
				else{
					$num = 0;
				}
			}
			else{
				if($char =~ /[AEIOUaeiou]/){
					$last = 1;
					$num++;
				}
				else{
					$last = 0;
					$num = 0;
				}
			}

			if($num >= 3){
				$consecutiveflag = 1;
			}

		}
		if($consecutiveflag){
			print ("$word ");
		}
	}
	
}
print("\n");
