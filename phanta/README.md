
* parse and replace

```
perl ./scripts/parse.pl --backup=data/backup.xml --keywords=data/uniq_keywords.tsv
```

* pretty print xml

```
bash ./scripts/prettize_xml.bash data/backup.xml > data/pretty_backup.xml
bash ./scripts/uniq_keywords.bash data/keywords.txt > data/uniq_keywords.txt
```

* 差分チェック

```
perl ./scripts/parse.pl --backup=data/backup.xml --keywords=uniq_keywords.tsv --check | sort > /tmp/a.log && \
cat /tmp/a.log | perl -nle '$_ =~ s/　/ /g; $_ =~ s/\s+//g; print $_;' | sort > /tmp/c.log && \
cat uniq_keywords.tsv | perl -nle 'print $1 if $_ =~ /(.*?)\t/' | perl -nle '$_ =~ s/　/ /g; $_ =~ s/\s+//g; print $_;' | sort > /tmp/b.log
```
