<title>${bf.config.blog.name}</title>
<link rel="alternate" type="application/rss+xml" title="RSS 2.0" href="${bf.util.site_path_helper(bf.config.blog.path,'/feed')}" />
<link rel="alternate" type="application/atom+xml" title="Atom 1.0" href="${bf.util.site_path_helper(bf.config.blog.path,'/feed/atom')}" />

<link rel='stylesheet' href='${bf.config.filters.syntax_highlight.css_dir}/bootstrap.1.3.0.min.css' type='text/css' />
<link rel='stylesheet' href='${bf.config.filters.syntax_highlight.css_dir}/pygments_${bf.config.filters.syntax_highlight.style}.css' type='text/css' />
<style type="text/css">
html, body { background-color:#ddd; }
body { padding-top: 60px; }
.hero-unit h1 { margin-bottom:10px; }
div.post_prose { margin-top: 20px }
div.post_meta { color: #888 }
.row { background-color:#fff; margin:0 -20px 0 -20px;padding-top:20px; box-shadow:0 3px 10px rgba(0, 0, 0, 0.5)}
.blog_post_title { text-shadow: 3px 3px 3px #ccc }

table.docinfo,
table.field-list { border-collapse: collapse } 

table.docinfo tr th,
table.field-list tr th
{
border-right:1px solid #aaa;
background-color: #f5f5f5;
}

div.dedication,
div.abstract{ text-align: center }
div.dedication p.topic-title,
div.abstract p.topic-title{ font-weight:bold }

div.pygments_monokai {
  border-radius: 5px;/* CSS3草案 */
  -webkit-border-radius: 5px;/* Safari,Google Chrome用 */
  -moz-border-radius: 5px;/* Firefox用 */
}
/*
 * 
 */
.attention .first,
.caution .first,
.danger .first,
.error .first,
.note .first,
.hint .first,
.tip .first,
.tip .first,
.important .first,
.warning .first{
  font-weight:bold
}
.attention,
.caution,
.danger,
.error,
.note,
.hint,
.tip,
.important,
.warning {
    background-repeat: repeat-x;
    border-radius: 4px 4px 4px 4px;
    border-style: solid;
    border-width: 1px;
    margin-bottom: 18px;
    position: relative;
    text-shadow: 0 1px 0 rgba(255, 255, 255, 0.5);
    background-image: none;
    box-shadow: none;
    padding: 10px;
    color: #404040;
}
.attention,
.caution,
.warning {
    background-color: #FDF5D9;
    border-color: #FCEEC1;
    color: #404040;
}
.error,
.danger{
    background-color:#FDDFDE;
    border-color: #FBC7C6;
}
.tip,
.hint,
.note,
.important{
    background-color:#D1EED1;
    border-color: #BFE7BF;
}
.tip,
.important{
    background-color:#DDF4FB;
    border-color:#DDF4FB;
}
</style>


