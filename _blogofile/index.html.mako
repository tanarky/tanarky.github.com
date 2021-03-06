<%inherit file="base.mako" />
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html>
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
    <title>Home - ${bf.config.blog.name}</title>
    <%include file="head.mako" />
    <style>h2 {font-style:Italic}</style>
  </head>
  <body>
    <%include file="header.mako" />

    <div class="container">
      <div class="row">
        <div class="span16">
      <!-- Main hero unit for a primary marketing message or call to action -->
      <div class="hero-unit">
        <h1>Stay hungry, Stay foolish.</h1>
        <p>Again, you can't connect the dots looking forward; you can only connect them looking backwards.
          So you have to trust that the dots will somehow connect in your future.
          You have to trust in something — your gut, destiny, life, karma, whatever
          This approach has never let me down, and it has made all the difference in my life.</p>
        <p>
          <a href="http://news.stanford.edu/news/2005/june15/jobs-061505.html" target="_new" class="btn primary large">Read more &raquo;</a></p>
      </div>
      </div>


        <div class="span-one-third">
          <h2>Blog Articles</h2>
          <p>recent articles</p>
          <ul>
            % for post in bf.config.blog.posts[:5]:
            <li><a href="${post.path}">${post.title}</a></li>
            % endfor
          </ul>
          <p><a class="btn" href="${bf.util.site_path_helper(bf.config.blog.path)}">Read more &raquo;</a></p>
        </div>

        <div class="span-one-third">
          <h2>My Personal Links</h2>
          <p>Personal activities.</p>
          <ul>
            <li>github</li>
            <li>Google+</li>
            <li>Facebook</li>
            <li>twitter</li>
            <li>LinkedIn</li>
          </ul>
        </div>

        <div class="span-one-third">
          <h2>Related sites</h2>
          <p>thanks.</p>
          <ul>
            <li>Yahoo!Japan</li>
            <li>Yahoo!Japan Shopping</li>
            <li>Yahoo!Japan Auctions</li>
          </ul>
        </div>

        <div class="span16">
          <%include file="footer.mako" />
        </div>
      </div>
    </div>
  </body>
</html>
