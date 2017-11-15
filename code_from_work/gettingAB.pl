#! /usr/bin/perl -w

use strict;
use warnings;

my $file = $ARGV[0];
open(FH, "<", $file) or die "Can't open file $!";

while (my $line = <FH>){
	chomp;
	my @data = split /\t/, $line;
	if($data[4] != 0){
		my $outfile = $file . "AB"
		open(OUT_FH, ">", $outfile) or die "Can't open file $outfile ($!)"; 
		print $outfile, $_;
		close OUT_FH;
		}
}
close FH; 