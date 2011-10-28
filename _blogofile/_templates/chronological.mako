<%inherit file="base.mako" />
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html>
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
    <title>Blog - ${bf.config.blog.name}</title>
    <%include file="head.mako" />
  </head>
  <body>
    <%include file="header.mako" />

    <div class="container">
      <div class="row">
        <div class="span12">

          <ul class="breadcrumb">
            <li><a href="/">Home</a> <span class="divider">&gt;</span></li>
            <li class="active"><h1>Blog<h1></li>
          </ul>

% for post in posts:
  <%include file="post.mako" args="post=post" />
% if bf.config.blog.disqus.enabled:
  <div class="after_post"><a href="${post.permalink}#disqus_thread">Read and Post Comments</a></div>
% endif
  <hr class="interblog" />
% endfor
% if prev_link:
 <a href="${prev_link}">« Previous Page</a>
% endif
% if prev_link and next_link:
  --  
% endif
% if next_link:
 <a href="${next_link}">Next Page »</a>
% endif

        </div>

        <div class="span4">
          <%include file="recent_articles.mako" />
        </div>

        <div class="span16">
          <%include file="footer.mako" />
        </div>
      </div>

    </div>
  </body>
</html>
