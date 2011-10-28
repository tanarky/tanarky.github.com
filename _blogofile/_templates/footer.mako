<footer>
  <p>&copy; 2011 tanarky</p>
</footer>

% if bf.config.blog.disqus.enabled:
<p><a href="http://${bf.config.blog.disqus.name}.disqus.com/latest.rss">Comments</a>.</p>
<br>
<div id="disqus_thread"></div>
<script type="text/javascript">
//<![CDATA[
    var disqus_shortname = 'tanarky';
    /* * * DON'T EDIT BELOW THIS LINE * * */
    (function() {
        var dsq = document.createElement('script'); dsq.type = 'text/javascript'; dsq.async = true;
        dsq.src = 'http://' + disqus_shortname + '.disqus.com/embed.js';
        (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(dsq);
    })();
//]]>
</script>
<a href="http://disqus.com" class="dsq-brlink">blog comments powered by <span class="logo-disqus">Disqus</span></a>
% endif
