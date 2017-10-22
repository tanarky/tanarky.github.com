#!/bin/bash

cat $1 | perl -nle 'foreach $l ( split "\t" ){ print $l if $l ne "" }' | sort -u
