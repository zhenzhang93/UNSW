#!/usr/bin/perl -w

#array

@myarr = (1..5);
$a=shift(@myarr);

print "$a\n","$a is shity,so we have 4 elements now","\n";

foreach $i (@myarr)
{
	printf("this is $i\n");
}
	


#hash

%hash_A=("123"=>"value1",123=>"value2",1=>"1",2=>"2");

#%hash_B{"key1"}=1;

#its is an empty hash
%hash_C=();
printf "the value of hahs_A of a is $hash_A{\"123\"}\n";

foreach my $key(keys(%hash_A)){
	printf ("$key +++++ $hash_A{$key}\n");
}

#子程序
sub printsomething
{
	printf "diyige sub,hanshu\n";
}	

&printsomething();
