<div class="well">
  <h5>Recent Articles</h5>
  <ol>
    % for rp in bf.config.blog.posts[:5]:
    <li><a href="${rp.path}">${rp.title}</a></li>
    % endfor
  </ol>
</div>
