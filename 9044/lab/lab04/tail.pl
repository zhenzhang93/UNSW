#!/usr/bin/perl -w

my $default_line=10;
if( $#ARGV >= 0 && $ARGV[0] =~ /^-[0-9]*$/){
	$ARGV[0] =~ s/-//;
#	print "$ARGV[0]\n";
	$default_line = $ARGV[0];
	shift(@ARGV);
}
#print "$default_line\n";

if ($#ARGV < 0){
	my @content = <STDIN>;
	while(@content > $default_line){
		shift(@content);
	}
	foreach (@content){
		print "$_";
	}	
}

else{	
	foreach $file(@ARGV){
		
		open(my $F, '<', $file) or die"$0 Can't open $file\n";
		my @file_content=<$F>;
		while(@file_content > $default_line){
			shift(@file_content);
		}
		if (@ARGV > 1){
          	 print "==> $file <==\n";
		}
		foreach(@file_content){
			print "$_";
		}
		close $F; 						
		
	}	
}
			
#$first=@file_content - $default_line;
#$first = 0 if $fist < 0;
#print @content[$first..$#content];
	




