#!/usr/bin/perl -w



if (@ARGV ge 2){

	foreach $file(@ARGV){

		open(F,'<',$file) or die;
		my @lines = ();
		
		while(my $content = <F>){
			push @lines,$content;
		}		
		close F;

		foreach $anotherfile(@ARGV){
			
			if ($file eq $anotherfile){
				next;
			}
			
			open(F2,'<',$anotherfile) or die;
			my @anotherlines = ();

			while(my $anothercontent = <F2>){
				push @anotherlines,$anothercontent;
			}	
			close F2;

			if(@lines ne @anotherlines){

				print "$anotherfile is not identical\n";
				exit 0;
			}

			for (my $i=0;$i<@lines;$i++){		
				if ($lines[$i] ne $anotherlines[$i]){
					print "$anotherfile is not identical\n";
					exit 0;
				}

			}


			

			
		}
		


	}
	print "All files are identical\n";

}

else{

	print "Usage: ./identical_files.pl <files>\n";
	exit 1;
}
















