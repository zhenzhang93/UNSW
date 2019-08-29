#!/usr/bin/perl -w

#use File::Basename;
#use File::Compare;

use File::Compare;
use File::Basename;

if(@ARGV ==2 ){

	for my $file(glob "$ARGV[0]/*"){
		my $basefile = basename($file);

		if( -e "$ARGV[1]/$basefile"){
			if(compare("$ARGV[1]/$basefile",$file) == 0){
				print "$basefile\n";
			}
		}
	}
}
