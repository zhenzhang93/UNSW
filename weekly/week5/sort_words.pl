#!/usr/bin/perl -w

#while(my $line = <STDIN>){
#	my @arr = split(/\s+/,$line);
#	print join(' ',sort @arr),"\n";

#}

my @res;
while(my $line = <STDIN>){
	
	chomp $line;
	@arr = split(/ +/,$line);

	push @res,join(" ",sort @arr),"\n";
}
print @res;
