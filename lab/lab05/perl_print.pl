#!/usr/bin/perl -w

if (@ARGV ne 1){
	print "usage: perl_print.pl arguement\n";
	exit 1;
}	

$ARGV[0] =~ s/\\/\\\\/g;
$ARGV[0] =~ s/"/\\"/g;


print "print \"$ARGV[0]\\n\";\n";
