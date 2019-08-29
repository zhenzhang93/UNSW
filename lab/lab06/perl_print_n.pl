#!/usr/bin/perl -w



if (@ARGV ne 2){
	print "usage: perl_print.pl arguement\n";
	exit 1;
}	


sub myprint{
	my $content = $_[0];
	$content =~ s/\\/\\\\/g;
	$content =~ s/"/\\"/g;
	print "print \"$content\\n\";\n";

}

if($ARGV[0] != 0 ){
	
	my $content = $ARGV[1];
	$content =~ s/\\/\\\\/g;
	$content =~ s/"/\\"/g;

	$string = "";
	for(my $i =1 ; $i < $ARGV[0]; $i++){
		$string =$string."print \""
	}
	$string .= "print \"$content\\n\"";

	
	print $string;
	
}
