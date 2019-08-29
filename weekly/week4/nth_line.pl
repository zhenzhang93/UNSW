#!/usr/bin/perl -w



# if(@ARGV ==2 ){
# 	open (F,'<',$ARGV[1]) or die;
# 	@content = <F>;
	
# 	if($ARGV[0] <= @content){
# 		print "$content[$ARGV[0]-1]";
	
# 	}
# 	close F;
# }



my @arr;
open(F,'<',$ARGV[1]) or die;
while (my $line = <F>){
	push @arr,$line;
}
print $arr[$ARGV[0]-1] if $ARGV[0]-1 <= $#arr;
close F;