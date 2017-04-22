$(document).ready(function() {
    var newerLink = $('a.blog-pager-newer-link').attr('href');
    $('a.blog-pager-newer-link').load(newerLink + ' .post-title:first', function() {
        var newerLinkTitle = $('a.blog-pager-newer-link').text();
        $('a.blog-pager-newer-link').html('<h4><b>← Previous Story</b></h4><h3>' + newerLinkTitle + '<h3>')
    });
    var olderLink = $('a.blog-pager-older-link').attr('href');
    $('a.blog-pager-older-link').load(olderLink + ' .post-title:first', function() {
        var olderLinkTitle = $('a.blog-pager-older-link').text();
        $('a.blog-pager-older-link').html('<h4><b>Next Story →</b></h4><h3>' + olderLinkTitle + '</h3>')
    })
});
