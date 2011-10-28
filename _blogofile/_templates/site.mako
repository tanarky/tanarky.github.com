<%inherit file="base.mako" />
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html>
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
    <%include file="head.mako" />
  </head>
  <body>
    <%include file="header.mako" />

    <div class="container">
      <div class="row">
        <div class="span12">
          ${next.body()}
        </div>

        <div class="span4">
          <div class="well">
            <h5>Recent Articles</h5>
            <ul>
              % for post in bf.config.blog.posts[:5]:
              <li><a href="${post.path}">${post.title}</a></li>
              % endfor
            </ul>
          </div>
        </div>

        <div class="span16">
        <%include file="footer.mako" />
        </div>
      </div>

    </div>
  </body>
</html>
