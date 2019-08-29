#!/usr/bin/perl -w


@number=<STDIN>;

$length = @number;

@lis=();

while(@lis< $length){
	my $num = int(rand($length+1));
	if ( grep( /^$num$/, @lis) ) {
  		next;
	}
	push(@lis,$num);	 

}

for(my $i = 0; $i < $length; $i++){
	print "$lis[$i]\n";
}
