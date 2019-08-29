#!/usr/bin/perl -w 

use File::Copy;

# my @arr=<>;

# foreach my $line(@arr){
# 	if($line =~ m/\d (\d\d):\d\d:\d\d/){
# 		$gai = $1;
		
# 		if($gai >=12){
# 			if($gai == 12){
# 				$line =~ s/(\d) \d\d:(\d\d):(\d\d)/$1 $gai:$2:$3pm/ ;
# 			}
# 			else{
# 				$gai -=12;
# 				if($gai<10){
# 					$gai = '0'.$gai;

# 				}
# 				$line =~ s/(\d) \d\d:(\d\d):(\d\d)/$1 $gai:$2:$3pm/ ;
				
# 			}

# 		}
# 		else{
# 			$line =~ s/(\d) \d\d:(\d\d):(\d\d)/$1 $gai:$2:$3am/ ;
# 		}
# 		print $line;
# 	}	
# }

#print ((sort{$myhash{$b} <=> $myhash{$a}} keys %myhash)[0],"\n");


#---------------------------------------
#my @arr = <>;

#foreach my $line(@arr){

#	while($line =~ /(\d+\.\d+)/){
#		
#		$newnum = sprintf("%.0f",$1);
#		$line =~ s/$1/$newnum/;
#	}
#	print $line;
#}

#another way of above


# foreach my $line(<>){
# 	my @arr = $line =~ /(\d+\.\d+)/g;
# 	#print $1;  it prints the last group that was captured
# 	#print @arr;
# 	foreach $mynum(@arr){
# 		$newnum=int($mynum+ 0.5);
# 		$line =~ s/$mynum/$newnum/g;
# 	}

# 	print $line;

# }


#----------------------------------------------

# open(F,'<',$ARGV[0]) or die;
# my @arr = <F>;
# close F;
# foreach my $line(@arr){
# 	$line =~ s/$ARGV[1]/($ARGV[1])/g;
# 	print $line;
# }

#----------------------------------------------


#while (my $line = <STDIN>){
#	$line =~ /(aabb)(cd)/g;
#	print $1;
#	print $2;
#	print $&;
#print all the () captured content

#}


#while(my $line = <STDIN>){
#	if($line =~ /\|([A-Z][a-z]*), ([A-Z][^|]*)/){
#		$fist=$1;
#		$second = $2;
#		$line =~  s/$fist, $second/$second $fist/g;
#	}
#	print $line;

#}


# while(my $line =<>){
# 	if($line =~ /([a-z]*) +(\d+)/){
# 		$h{$1} += $2;

# 	}
# }
# $key = (sort{$h{$b} <=> $h{$a}} keys %h)[0];

# print "Expel $key total $h{$key}","\n";



#using the 'e', the int() can be regarded as expression, not just a string.
#s/(\d+\.\d+)/int($& + 0.5)/eg;


#$a="abacAAA";
#print uc($a);

#week4 q11

#while (my $line =<>){
#	$line =~ s/[aeiou]//ig;
#	print $line;
#}

#-p
#tr /aeiouAEIOU//d ;


#question 12

# my $num = 10;
# if ($ARGV[0] =~ /-[0-9]+/){
	
# 	if($ARGV[0] =~ /-[0-9]+/){
		
# 		$ARGV[0] =~  s/-//;
# 		$num=$ARGV[0];
# 		shift @ARGV;
# 	}
# }


# foreach my $file(@ARGV){
# 	my $count = 0;
# 	# open(F,'<',$file) or die;
# 	# while(my $line =<F>){
# 	# 	if($count <= $num){
# 	# 		$count = $count + 1;
# 	# 		print $line;
# 	# 	}	
# 	# 	else{
# 	# 		close F;
# 	# 		last;
# 	# 	}
# 	# }

# 	#another way

# 	open(F,'<',$file) or die;
# 	@arr = <F>;
	
# 	print @arr[$count..$num];
# 	close F;
# }

#my @arr= <STDIN>;


#print reverse @arr;

#for(my $i = $#arr; $i >=0; $i--){
#	print $arr[$i];
#}

# $lines = 1;

# while(my $line = <STDIN>){
# 	printf ("%6d        ",$lines++);
# 	chomp $line;
# 	foreach $c (split(//,$line)){
# 		if(ord($c) >32 ){
# 			print $c;
# 		}
# 		else{
# 			print "^".chr(ord($c)+64);
# 		}
# 	}
# 	print "\$\n";
# }

#my $num=$ARGV[0];
#@arr = <STDIN>;

#foreach $i(0..$num){
#	push @res,$arr[$i];
#}
#print join("",@res);



#week5 q11

#while(my $line = <STDIN>){

#	if($line =~ /([a-z]+) +([a-z]+)\(([a-z]+ *[^a-zA-Z]*) ([^\)]+)\) *{/){
#		print $1,"\n",$2,"\n",$3,"\n",$4,"\n";
#	}
#}


#q12
# sub include_file($) {
#     my ($file) = @_;
#     # this function is recursive so a local filehandle is essential
#     open my $f, '<', $file or die "$0: can not open $file: $!";
#     while ($line = <$f>) {
#         if ($line =~ /^#\s*include\s*"([^"]*)"/) {
#             include_file($1);
#         } else {
#             print $line;
#         }
#     }
#     close $f;
# }

# foreach $file (@ARGV) {
#     include_file($file);
# }


#open(F,'<',"8.txt") or die "OJBK $!";

#Q13

# sub printfile{
# 	foreach $file(glob "$ARGV[0]"){
# 		# ""
# 		if ($line =~ /^#include\s*"([^"]*)"/)
# 			printfile();
# 		# <>
# 		elsif ($line =~ /^#include\s*<([^>]*)>/)
# 			printfile();
# 		else{
# 			print;
# 		}
# 	}
# }

#Q14,WC function

#foreach $file (glob("*.[ch]"))
#foreach my $file(glob "*"){
#	open(F,'<',$file) or die;
#	@arr = <F>;
#	$num = @arr;
#	printf ("%5d %s",$num,$file);
#	print "\n";
#	close F;	

#}


#Q15

#remember this one;
#system "cat $ARGV[0]";

#@arr=<>;
#while (<>){

#	@num = split(//,$_);
#	print "@num";
#	print @num;
#}

#print $#arr + 1 ,"\n";

#q17

#while(my $line =<>){
#	my ($id,$name,$address,$city) = split(/,/,$line);
#	print $id;

#}



#week6 q5

#while(my $line =<>){
#	if($line =~ /[a-z]+/){

#		$myhash{$line} +=1;
#	}
#}
#foreach my $key (sort{$myhash{$a} <=> $myhash{$b} or ${a} cmp ${b}} keys %myhash){
#	printf ("%4d the value is %s",$myhash{$key},$key);
#}

#Q6.

#while(<>){
#	$myhash{$_} +=1;
#}
#foreach my $key(sort keys %myhash){
#	print $key;
#}


#Q7
# while(my $line = <>){
# 	($date,$num,@name) = split(/\s+/,$line);
# 	$myhash{"$date @name"} +=$num;
# }
# foreach $ele(@name){
#     print "$ele\n";
# }
# print "@name";
# foreach my $key(keys %myhash){
# 	my ($data,@name) = split(/ /,$key); 
# 	print "$data+++$myhash{$key} ++@name";
# 	print "\n";
# }

#/^([^ ]+)\s+(\d+)\s+(.+)\s*$/

# @arr = (12,5,8);
# print "@arr";


#week Q9

#foreach my  $url(@ARGV){
#	open(F,'<',"wget -q -O $url") or die;


#while(my $line = <>){
#	@arr = split(/[^\d\- ]/,$line);
#	foreach my $e(@arr){
#		if($e =~ /\d+/){
#			print "$e\n";
#		}
#	}

#}

#} 

#foreach $n (1..10) {
#    last if ($n > 5);
#    print "$n ";
#    next if ($n % 2 == 0);
#    print "$n ";
#}
#print "\n";

#Q13


#split(/\W+/,$line);
# while(my $line = <STDIN>){
# 	$line =~ s/\W*$//g;
# 	push @arr,$line;
# }

# my $newline=join("",@arr);
# @words = split(/[^a-zA-Z]/,$newline);
# foreach my $word(@words){
# 	$w{$word} +=1;
# }
# foreach my $key (sort keys %w){
# 	print "$key ++ $w{$key}\n";
# }
# for(my $i = 0; $i < @words- 2; $i++){
# 	$fre{$words[$i]}{$words[$i+1]} +=1;
# }
# foreach my $key (sort keys %fre){
# 	print "$fre{$key}\n";
# 	foreach $num (sort{$fre{$key}{$a} <=> $fre{$key}{$b}} keys %{$fre{$key}} ){
# 		print "$key --- $fre{$key}{$num}\n";
# 	}	
# }



#wee6 Q14:

#@arr = <STDIN>;
#print "\n<li>\n<ul>".join("<ul>",@arr)."\n</li>\n";


#Q22

#my @res;
#while(my $line = <>){

#	@arr = $line =~ /< *\/([^>]+)>/g;
#	push @res,@arr;	
#}
#print "@res\n";


#%myhash=('a'=>6,'ab'=>5);
#@sortedkey = sort{${a} cmp ${b}} keys %myhash;
#print "$_   ++  $myhash{$_}\n" foreach @sortedkey;

#$a=15.555;
#printf "%6.1f",$a;


#%w = ("2"=>5,"3"=>8,"4"=>8,"a"=>8);
#while( my($key,$value) = each %w){
#	print "$key,$value\n";
#}

#week10 Q14
#while(my $line =<>){
#	chomp $line;
#	my @arr = split(/ +/,$line);	
#	@arr = reverse @arr;
#	$newline = join (" ",@arr);
#	print "@arr\n";
#	print "$newline\n";
#}

# @arr = <STDIN>;
# if (@arr>1){
# 	print "Not hill";
# } 
# else{
# 	foreach my $num(split(/\s+/,@arr)){
# 		$last = $num if $count;
# 		if($last){
# 			if($num > $last ){
# 				if($flag && $flag == 0){
# 					print "No hill";
# 					exit 0;
# 				}
# 				$apper = 1;
# 				$flag = 1;
# 			}
# 			elsif($num < $last){
# 				if($flag && $flag ==1){
# 					print "No hill";
# 					exit 0;
# 				}
# 				$xiaapper = 1;
# 				$flag = 0;
# 			}
# 			else{
# 				print "No hill";
# 				exit 0;
# 			}
# 		}	
# 		$count +=1;
# 	}
# 	if($apper && $xiaapper){
# 		print "hill";
# 	}
# 	else {print "Not hill"};
	
# } 

#@arr = <>;
#@newarr = split(/\D+/,join(" ",@arr));
#print "@newarr\n";
#print $newarr[0],"\n";

# foreach my $arg (@ARGV){
# 	$w{$arg} += 1;
# }	

# foreach my $key(keys %w){
# 	$neww{$key} = $key  * $w{$key}; 
# }
# while(my ($key,$value) = each %neww){
# 	print "$key++++$value\n";
# }
# print ((sort{ $neww{$b} <=> $neww{$a}} keys %neww)[0], "\n");


#my @res;
#while(my $line = <>){
#	@arr = $line =~ /\w+/g;
#	push @res,@arr;
#}

#print "@res\n";


while ($line = <>) {
    @numbers = $line =~ /[\d\- ]+/g;
	print "@numbers\n";
    foreach $number (@numbers) {
        $number =~ s/\D//g;
		print $number,"\n";
        print "$number\n" if length $number >= 8 && length $number <= 15;
    }
}

























