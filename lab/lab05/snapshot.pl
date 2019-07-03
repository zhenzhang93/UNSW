#!/usr/bin/perl -w

use File::Copy;

$number = 0;
while(-d ".snapshot.$number"){
	$number++;
}

if($ARGV[0] eq "save"){

	mkdir ".snapshot.$number";
	$path = ".snapshot.$number";
	foreach my $file(glob "*"){
		next if ($file =~ /^\./);
		next if ($file =~ /snapshot.pl/);
		copy($file,$path) or die;
	}
	print "Creating snapshot $number\n";

}

if($ARGV[0] eq "load"){

	if(-d ".snapshot.$ARGV[1]"){
		mkdir ".snapshot.$number";
		$path = ".snapshot.$number";
		foreach my $file(glob "*"){
			next if ($file =~ /^\./);
			next if ($file =~ /snapshot.pl/);
			copy($file,$path) or die;
		}
		print "Creating snapshot $number\n";
		foreach my $file(glob ".snapshot.$ARGV[1]/*"){	
			copy ($file, ".") or die;
		}
		print "Restoring snapshot $ARGV[1]\n";

	}

}

















