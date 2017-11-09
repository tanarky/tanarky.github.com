#!env perl

use utf8;
use strict;
use warnings;
use Data::Dumper;
use Getopt::Long;
use HTML::Entities;
use Encode;
#use open IN  => ":utf8";

my %opts = ();
GetOptions(
    '-backup=s'   => \$opts{backup},
    '-keywords=s' => \$opts{keywords},
    '-check'      => \$opts{check},
);

my $pattern_entry   = '<entry><id>tag:blogger.com,1999:blog-6144655530126189217.post-(\d+)</id>(.*?)</entry>';
my $pattern_cats    = "<category scheme='http://www.blogger.com/atom/ns#' term='(.*?)'/>";
my $pattern_title   = "<title type='text'>(.*?)</title>";
my $pattern_content = "<content type='html'>(.*?)</content>";
my $xml = `cat $opts{backup}`;
#my @keywords = map { my @k = map { $_ =~ s/　/ /g; $_ =~ s/\s$//; $_ } split "\t"; [@k] } split "\n", `cat $opts{keywords}`;
my @keywords = map { my @k = map { $_ =~ s/　/ /g; $_ =~ s/\s+//g; $_ } split "\t"; [@k] } split "\n", `cat $opts{keywords}`;

my @ids = ();
while($xml =~ /$pattern_entry/g){
    my $blog_id = $1;
    my $entry   = $2;
    my $content = '';
    my $cats    = [];
    my $fn;
    my $fh;
    my $title   = '';

    # parse
    if($entry =~ /$pattern_title/){
        $title = decode_entities($1);
        $title =~ s/　/ /g;
        $title =~ s/\s+//g;
    }
    if($entry =~ /$pattern_content/){
        $content = decode_entities($1);
        $content =~ s|<br \/>|<br \\>\n|g;
    }
    #while($entry =~ m|$pattern_cats|g){
    #    push @$cats, $1;
    #}
    ##warn Dumper($cats);

    # dump origin article body
    $fn = "origin/" . $blog_id. ".txt";
    open($fh, ">", "$fn") or die;
    print $fh $content;
    close($fh);

    # check title and emphasize keywords
    my $found = 0;
    foreach my $k (@keywords) {
        my ($t, @kk) = @$k;
        
        # strong keywords
        if($t eq $title){
            $found++;
            foreach my $k (@kk){
                $content =~ s|($k)|<b>$1</b>|g;
            }
        }
    }
    # check if matched title
    next if !$found;
    if($opts{check}){
        print $title. "\n";
        next;
    }

    # cleanup html
    $content =~ s|font-family: (.*?), sans-serif;||g;
    $content =~ s|color: #333333;  font-size: 15px; ?||g;
    $content =~ s|box-sizing: border-box; ?||g;
    $content =~ s|background-color: white; ?||g;
    $content =~ s|text-align: justify; ?||g;
    $content =~ s|font-size: 15px; ?||g;
    $content =~ s| style=""||g;
    $content =~ s|<b><b>|<b>|g;
    $content =~ s|</b></b>|</b>|g;
    while($content =~ /((alt|title)="(.*?)")/g){
        my $attr_all  = $1;
        my $attr_name = $2;
        my $attr_body = $3;
        if(index($attr_body, '<b>') != -1){
            my $attr_org = $attr_all;
            $attr_body =~ s|</?b>||g;
            $attr_all  = $attr_name. '="'. $attr_body. '"';
            $content =~ s|$attr_org|$attr_all|g;
        }
    }
    while($content =~ m|(<(h[2-3])>(.*?)</h[2-3]>)|g){
        my $h2_all  = $1;
        my $h2_name = $2;
        my $h2_body = $3;
        if(index($h2_body, '<b>') != -1){
            my $h2_org = $h2_all;
            $h2_body =~ s|</?b>||g;
            $h2_all  = '<'. $h2_name. '>'. $h2_body. '</'. $h2_name. '>';
            $content =~ s|$h2_org|$h2_all|g;
        }
    }

    # dump new html
    $fn = "new/" . $blog_id. ".txt";
    open($fh, ">", "$fn") or die;
    print $fh $content;
    close($fh);

    # store blog id and title
    if($title){
        push @ids, {id => $blog_id, title => decode_utf8($title)};
    }
}

# dump index.html
my $fn = "index.html";
open(my $fh, ">:encoding(utf8)", "$fn") or die;
print $fh '<!doctype html>';
print $fh '<html><head><meta charset="utf-8"><link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous"></head><body><div class="container"><div class="row"><div class="col-md-12">';
print $fh '<table class="table table-bordered">'. "\n";
foreach my $id (@ids) {
    my $i = $id->{id};
    my $t = $id->{title};
    my $link = 'https://www.blogger.com/blogger.g?blogID=6144655530126189217#editor/target=post;postID='.$i.';onPublishedMenu=allposts;onClosedMenu=allposts;postNum=0;src=link';
    print $fh '<tr>'. "\n";
    print $fh '<td>'. $t. '</td>'. "\n";
    print $fh '<td><a target="_blank" href="origin/'. $i. '.txt">オリジナル本文</a></td>'. "\n";
    print $fh '<td><a target="_blank" href="new/'. $i. '.txt">新本文</a></td>'. "\n";
    print $fh '<td><a target="_blank" href="'. $link. '">blogger編集ページ</a></td>'. "\n";
    print $fh '</tr>'. "\n";
}
print $fh '</div></div></div></table></body></html>'. "\n";
close($fh);
