#!/usr/bin/perl -w



$length = @ARGV;
open (F, '>', $ARGV[2]) or die;
if($length == 3){
	for($i = $ARGV[0]; $i <=$ARGV[1];$i=$i+1){
		print F "$i\n";
	}
}

close F;
