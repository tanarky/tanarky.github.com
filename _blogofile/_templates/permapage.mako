<%inherit file="base.mako" />
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html>
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
    <title>${post.title} - ${bf.config.blog.name}</title>
    <%include file="head.mako" />
  </head>
  <body>
    <%include file="header.mako" />

    <div class="container">
      <div class="row">
        <div class="span12">

          <ul class="breadcrumb">
            <li><a href="/">Home</a> <span class="divider">&gt;</span></li>
            <li><a href="/blog">Blog</a> <span class="divider">&gt;</span></li>
            <li class="active"><h1>${post.title}<h1></li>
          </ul>

          <%include file="post.mako" args="post=post" />

<br/>
% if bf.config.blog.disqus.enabled:
<a href="https://twitter.com/share" class="twitter-share-button" data-count="horizontal" data-via="tanarky" data-lang="ja">ツイート</a><script type="text/javascript" src="//platform.twitter.com/widgets.js"></script>
<div id="disqus_thread"></div>
<script type="text/javascript">
  var disqus_url = "${post.permalink}";
</script>
<script type="text/javascript" src="http://disqus.com/forums/${bf.config.blog.disqus.shortname}/embed.js"></script>
<a href="http://disqus.com" class="dsq-brlink">blog comments powered by <span class="logo-disqus">Disqus</span></a>
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

