//<![CDATA[
var classicMode = false ;
var summary = 40;
var indent = 3;
imgr = new Array();
imgr[0] = "http://2.bp.blogspot.com/-mmjt8mh87bQ/VQ6ltMr8GxI/AAAAAAAAEfo/93SmjxkwmO0/s1600/no-image-found.jpg";
showRandomImg = true;
aBold = true;
summaryPost = 220; 
summaryTitle = 25; 
numposts1 = 5; 
numposts2 = 8;
var classicMode = false ;
var summary = 50;
var indent = 3;
var relatedTitles = new Array();
var relatedTitlesNum = 0;
var relatedUrls = new Array();
var thumburl = new Array();


function stripHtmlTags(s,max){return s.replace(/<.*?>/ig, '').split(/\s+/).slice(0,max-1).join(' ')}
function createSummaryAndThumb(pID,title,url,date,comment,tag,author){
    var posturl= url;
    var title=title;
    var date = date;
    var comment = comment;
    var tag = tag;
    var div = document.getElementById(pID);
    var img = div.getElementsByTagName("img");
    var content1 = div.innerHTML.replace(/<img.*?>/ig,'').replace(/<iframe.*?>/ig,''); 
    var arr = content1.split(/<br\s*\/?>/);
    var content = arr[0]+arr.slice(1,-1).join('<br>')+arr.slice(-1);
    var month = new Array();
    month[0] = "Jan";
    month[1] = "Feb";
    month[2] = "Mar";
    month[3] = "Apr";
    month[4] = "May";
    month[5] = "Jun";
    month[6] = "Jul";
    month[7] = "Aug";
    month[8] = "Sep";
    month[9] = "Oct";
    month[10] = "Nov";
    month[11] = "Dec";
    var n = month[date.split('/')[0]];
    var date1 = date.split('/')[1];
    var year = date.split('/')[2];



    
    if(img.length ==1) {
	    var imgurl=img[0].src;
	    var thumb = '<div class="post-image"><a href="'+posturl+'"><img width="675" height="450" src="'+imgurl+'"></a></div>';
	    var summary1 = thumb+'<div class="post-entry">'+stripHtmlTags(content,65)+'...</div>';
	}
    else {
        if(img.length > 1) {
		    var li = '';
		    for(var i=0; i<img.length; i++){
			    var li = li + '<li><img src="'+img[i].src+'"></li>';	
		    }
		    var thumb = '<div class="post-image"><div class="bx-wrapper"><ul class="bxslider">'+li+'</ul></div></div>';
		    var summary1 = thumb+'<div class="post-entry">'+stripHtmlTags(content,65)+'...</div>';
	    }
        else {
		    var frame = div.getElementsByTagName("iframe");
		    if (frame.length >=1) {
			    var iframe1 = frame[0].src;
			    var thumb = '<div class="post-image"><iframe width="100%" height="450" frameborder="no" src="'+iframe1+'" scrolling="no"></iframe></div>';
			    var summary1 = thumb+'<div class="post-entry">'+stripHtmlTags(content,65)+'...</div>';
		    }
		    else {
			    var summary1 = '<div class="post-entry">'+stripHtmlTags(content,65)+'...</div>';
		    }
	    }   
    }
    
    
    
    
    div.innerHTML = summary1;
    div.style.display = "block";
    var elem = document.getElementsByClassName("separator");
    for (var i=0; i< elem.length; i++){
        elem[i].innerHTML='';
    }

}

function related_results_labels_thumbs(json) {
    for (var i = 0; i < json.feed.entry.length; i++) {
        var entry = json.feed.entry[i];
        relatedTitles[relatedTitlesNum] = entry.title.$t;
        try 
        {thumburl[relatedTitlesNum]=entry.media$thumbnail.url;}


        catch (error){

            s=entry.content.$t;a=s.indexOf("<img");b=s.indexOf("src=\"",a);c=s.indexOf("\"",b+5);d=s.substr(b+5,c-b-5);
            if((a!=-1)&&(b!=-1)&&(c!=-1)&&(d!=""))
            {thumburl[relatedTitlesNum]=d;} else {if(typeof(defaultnoimage) !== 'undefined') thumburl[relatedTitlesNum]=defaultnoimage; else thumburl[relatedTitlesNum]="http://2.bp.blogspot.com/-mmjt8mh87bQ/VQ6ltMr8GxI/AAAAAAAAEfo/93SmjxkwmO0/s1600/no-image-found.jpg";}

        }

        if(relatedTitles[relatedTitlesNum].length>35) relatedTitles[relatedTitlesNum]=relatedTitles[relatedTitlesNum].substring(0, 35)+"...";
        for (var k = 0; k < entry.link.length; k++) {
            if (entry.link[k].rel == 'alternate') {
                relatedUrls[relatedTitlesNum] = entry.link[k].href;
                relatedTitlesNum++;


            }
        }
    }
}
function removeRelatedDuplicates_thumbs() {
    var tmp = new Array(0);
    var tmp2 = new Array(0);
    var tmp3 = new Array(0);
    for(var i = 0; i < relatedUrls.length; i++) {
        if(!contains_thumbs(tmp, relatedUrls[i])) 
        {
            tmp.length += 1;
            tmp[tmp.length - 1] = relatedUrls[i];
            tmp2.length += 1;
            tmp3.length += 1;
            tmp2[tmp2.length - 1] = relatedTitles[i];
            tmp3[tmp3.length - 1] = thumburl[i];
        }
    }
    relatedTitles = tmp2;
    relatedUrls = tmp;
    thumburl=tmp3;


}
function contains_thumbs(a, e) {
    for(var j = 0; j < a.length; j++) if (a[j]==e) return true;
    return false;
}
function printRelatedLabels_thumbs(current) {
    for(var i = 0; i < relatedUrls.length; i++)
    {
        if((relatedUrls[i]==current)||(!relatedTitles[i]))
        {
            relatedUrls.splice(i,1);
            relatedTitles.splice(i,1);
            thumburl.splice(i,1);
            i--;
        }
    }


    var r = Math.floor((relatedTitles.length - 1) * Math.random());
    var i = 0;

    while (i < relatedTitles.length && i < 20 && i<maxresults) {
        tmb = thumburl[r].replace('s72-c/','s300-c/');

        document.write('<div class="item-related"><a href="' + relatedUrls[r] + '"><img width="150" height="100" src="'+tmb+'"/></a><h3><a href="' + relatedUrls[r] + '">'+relatedTitles[r]+'</a></h3></div>');i++;


        if (r < relatedTitles.length - 1) {
            r++;
        } else {
            r = 0;
        }

    }

    relatedUrls.splice(0,relatedUrls.length);
    thumburl.splice(0,thumburl.length);
    relatedTitles.splice(0,relatedTitles.length);

}
function removeHtmlTag(strx, chop) {
    var s = strx.split("<");
    for (var i = 0; i < s.length; i++) {
        if (s[i].indexOf(">") != -1) {
            s[i] = s[i].substring(s[i].indexOf(">") + 1, s[i].length)
        }
    }
    s = s.join("");
    s = s.substring(0, chop - 1);
    return s
}
function showrecentposts1(json) {
    j = (showRandomImg) ? Math.floor((imgr.length + 1) * Math.random()) : 0;
    img = new Array();
    if (numposts1 <= json.feed.entry.length) {
        maxpost = numposts1
    } else {
        maxpost = json.feed.entry.length
    }
    document.write('<div class="flexslider"><ul class="slides">');
    for (var i = 0; i < maxpost; i++) {
        var entry = json.feed.entry[i];
        var posttitle = entry.title.$t;
        var pcm;
        var posturl;
        var cate = '';
        for (var e = 0; e < json.feed.entry[i].category.length; e++) {
            cate = '<a href="/search/label/' + json.feed.entry[i].category[e].term + '?max-results=6">' + json.feed.entry[i].category[e].term + '</a>'
        }
        if (i == json.feed.entry.length) break;
        for (var k = 0; k < entry.link.length; k++) {
            if (entry.link[k].rel == 'alternate') {
                posturl = entry.link[k].href;
                break
            }
        }
        for (var k = 0; k < entry.link.length; k++) {
            if (entry.link[k].rel == 'replies' && entry.link[k].type == 'text/html') {
                pcm = entry.link[k].title.split(" ")[0];
                break
            }
        }
        if ("content" in entry) {
            var postcontent = entry.content.$t
        } else if ("summary" in entry) {
            var postcontent = entry.summary.$t
        } else var postcontent = "";

        postdate = entry.published.$t;
        if (j > imgr.length - 1) j = 0;
        img[i] = imgr[j];
        s = postcontent;
        a = s.indexOf("<img");
        b = s.indexOf("src=\"", a);
        c = s.indexOf("\"", b + 5);
        d = s.substr(b + 5, c - b - 5);
        if ((a != -1) && (b != -1) && (c != -1) && (d != "")) img[i] = d;
        var month = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12];
        var month2 = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
        var day = postdate.split("-")[2].substring(0, 2);
        var m = postdate.split("-")[1];
        var y = postdate.split("-")[0];
        for (var u2 = 0; u2 < month.length; u2++) {
            if (parseInt(m) == month[u2]) {
                m = month2[u2];
                break
            }
        }

        var tmb = img[i].replace('s320/','s1600/').replace('s400/','s1600/').replace('s640/','s1600/');


        var daystr = day + ' ' + m + ' ' + y;
        var trtd = '<li style="position: relative;" class="featured-post"><a class="thumb" href="' + posturl + '"><div  class="feets" style="background-image:url(' + tmb +');"></div></a><div class="slide-overlay "><div class="related-header"><div class="single-cat"><span class="cat">'+ cate +'</span></div><span class="meta-info"><span>'+ m +'</span> <span>'+ day +'</span>, <span>'+ y+'</span></span><h2><a href="' + posturl + '">' + posttitle + '</a></h2></div></div></li>';



        document.write(trtd);
        j++
    }
    document.write('</ul></div>')
}
function showrecentposts2(json) {
    j = (showRandomImg) ? Math.floor((imgr.length + 1) * Math.random()) : 0;
    img = new Array();
    if (numposts1 <= json.feed.entry.length) {
        maxpost = numposts1
    } else {
        maxpost = json.feed.entry.length
    }
    for (var i = 0; i < maxpost; i++) {
        var entry = json.feed.entry[i];
        var posttitle = entry.title.$t;
        var pcm;
        var posturl;
        var cate = '';
        for (var e = 0; e < json.feed.entry[i].category.length; e++) {
            cate = cate + '<a href="/search/label/' + json.feed.entry[i].category[e].term + '?max-results=6">' + json.feed.entry[i].category[e].term + '</a>, '
        }
        if (i == json.feed.entry.length) break;
        for (var k = 0; k < entry.link.length; k++) {
            if (entry.link[k].rel == 'alternate') {
                posturl = entry.link[k].href;
                break
            }
        }
        for (var k = 0; k < entry.link.length; k++) {
            if (entry.link[k].rel == 'replies' && entry.link[k].type == 'text/html') {
                pcm = entry.link[k].title.split(" ")[0];
                break
            }
        }
        if ("content" in entry) {
            var postcontent = entry.content.$t
        } else if ("summary" in entry) {
            var postcontent = entry.summary.$t
        } else var postcontent = "";
        postdate = entry.published.$t;
        if (j > imgr.length - 1) j = 0;
        img[i] = imgr[j];
        s = postcontent;
        a = s.indexOf("<img");
        b = s.indexOf("src=\"", a);
        c = s.indexOf("\"", b + 5);
        d = s.substr(b + 5, c - b - 5);
        if ((a != -1) && (b != -1) && (c != -1) && (d != "")) img[i] = d;
        var month = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12];
        var month2 = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
        var day = postdate.split("-")[2].substring(0, 2);
        var m = postdate.split("-")[1];
        var y = postdate.split("-")[0];
        for (var u2 = 0; u2 < month.length; u2++) {
            if (parseInt(m) == month[u2]) {
                m = month2[u2];
                break
            }
        }
        var tmb = img[i].replace('s1600/', 's500-c/');
        var daystr = day + ' ' + m + ' ' + y;
        var trtd = '<li><div class="side-item"><div class="side-image"><a href="' + posturl + '"><img width="150" height="100" src="' + tmb + '"></a></div><div class="side-item-text"><h4><a href="' + posturl + '">' + posttitle + '</a></h4><span class="side-item-meta">' + daystr + '</span></div></div></li>';
        document.write(trtd);
        j++
    }
}

function stripHtmlTags1(s){return s.replace(/<a.*?>/ig, '')}
function showrecentcomments(json) {
    for (var i = 0; i < 6; i++) {
        var entry = json.feed.entry[i];
        var ctlink;
        if (i == json.feed.entry.length) break;
        for (var k = 0; k < entry.link.length; k++) {
            if (entry.link[k].rel == 'alternate') {
                ctlink = entry.link[k].href;
                break;
            }
        }
        ctlink = ctlink.replace("#", "#comment-");
        var ptlink = ctlink.split("#");
        ptlink = ptlink[0];
        var txtlink = ptlink.split("/");
        txtlink = txtlink[5];
        txtlink = txtlink.split(".html");
        txtlink = txtlink[0];
        var pttitle = txtlink.replace(/-/g," ");
        pttitle = pttitle.link(ptlink);
        if ("content" in entry) {
            var comment = entry.content.$t;}
        else
            if ("summary" in entry) {
                var comment = entry.summary.$t;}
        else var comment = "";
        var re = /<\S[^>]*>>/g;
        comment = comment.replace(re, "");
        document.write('<li>');
        commentauthor1 = entry.author[0].name.$t;
        commentauthor = stripHtmlTags(commentauthor1,40);
        document.write('<div class="small"><i class="icon-comment-alt"></i> ' + commentauthor + '</div>');
        if (comment.length < 100) {
            document.write('<div class="comments-custom_txt"><a target="_blank" href="' + ctlink + '">'+stripHtmlTags1(comment)+ '</a></div>');
        }
        else
        {
            comment = comment.substring(0, 100);
            var quoteEnd = comment.lastIndexOf(" ");
            comment = comment.substring(0, quoteEnd);
            document.write('<div class="comments-custom_txt"><a target="_blank" href="' + ctlink + '">'+stripHtmlTags1(comment) + '...</a></div>');
        }
    }
    document.write('</li>');
}

function authorshow(data) {
    for (var i = 0; i < 1; i++) {
        var entry = data.feed.entry[i];
        var avtr = entry.author[0].gd$image.src;
        document.write('<img width="100" height="100" src="' + avtr + '"/>');

    }
}
