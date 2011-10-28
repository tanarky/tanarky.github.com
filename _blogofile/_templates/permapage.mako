<%inherit file="site.mako" />

<ul class="breadcrumb">
  <li><a href="/">Home</a> <span class="divider">&gt;</span></li>
  <li><a href="/blog">Blog</a> <span class="divider">&gt;</span></li>
  <li class="active"><h1>${post.title}<h1></li>
</ul>

<%include file="post.mako" args="post=post" />

% if bf.config.blog.disqus.enabled:
<div id="disqus_thread"></div>
<script type="text/javascript">
  var disqus_url = "${post.permalink}";
</script>
<script type="text/javascript" src="http://disqus.com/forums/${bf.config.blog.disqus.shortname}/embed.js"></script>
<a href="http://disqus.com" class="dsq-brlink">blog comments powered by <span class="logo-disqus">Disqus</span></a>
% endif
