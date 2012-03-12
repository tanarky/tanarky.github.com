#!/bin/sh

SITEMAP=./sitemap.xml
#BLOGOFILEBIN=/home/satoshi/.virtualenvs/2.7.2/bin/blogofile
BLOGOFILEBIN=blogofile

cd ./_blogofile
$BLOGOFILEBIN build
cd ..
rm -rf ./blog
cp -pr ./_blogofile/_site/* ./
echo '<?xml version="1.0" encoding="UTF-8"?>' > $SITEMAP
echo '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' >> $SITEMAP
find ./ -name "*html" | perl -nle 'print "<url><loc>http://tanarky.com$1</loc></url>" if($_ !~ m|40[34]\.html| && $_ !~ m|^\./_| && m|^\.(.*)|)' >> $SITEMAP
echo "</urlset>" >> $SITEMAP
