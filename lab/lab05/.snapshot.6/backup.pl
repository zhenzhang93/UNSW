#!/usr/bin/perl -w


if(@ARGV eq 1){
	
	$number = 0;
	$file = $ARGV[0];
	open (F,'<',$file) or die;

	while (-e ".$file.$number"){
		$number++;
	}
	
	open(IN,'>>',".$file.$number") or die;
	while($line = <F>){
		print IN $line;
	}
	close IN;
	print "Backup of '$file' saved as '.$file.$number'\n";
	close F;
}
