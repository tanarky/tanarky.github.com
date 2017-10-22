
#!env perl
use utf8;
use strict;
use warnings;
use Data::Dumper;
use Getopt::Long;

my %opts;
GetOptions('-words=s' => \$opts{words});
#warn Dumper(\%opts);
my @words = split ",", $opts{words};

while(<>){
    foreach my $w (@words) {
        warn $w;
        #$_ =~ s///g;
    }
}
