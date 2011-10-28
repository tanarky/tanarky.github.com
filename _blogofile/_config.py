# -*- coding: utf-8 -*-

######################################################################
# This is your site's Blogofile configuration file.
# www.Blogofile.com
#
# This file doesn't list every possible setting, it relies on defaults
# set in the core blogofile _config.py. To see where the default
# configuration is on your system run 'blogofile info'
#
######################################################################

######################################################################
# Basic Settings
#  (almost all sites will want to configure these settings)
######################################################################
## site_url -- Your site's full URL
# Your "site" is the same thing as your _site directory.
#  If you're hosting a blogofile powered site as a subdirectory of a larger
#  non-blogofile site, then you would set the site_url to the full URL
#  including that subdirectory: "http://www.yoursite.com/path/to/blogofile-dir"
site.url = "http://tanarky.com"

#### Blog Settings ####
blog = controllers.blog

## blog_enabled -- Should the blog be enabled?
#  (You don't _have_ to use blogofile to build blogs)
blog.enabled = True

## blog_path -- Blog path.
#  This is the path of the blog relative to the site_url.
#  If your site_url is "http://www.yoursite.com/~ryan"
#  and you set blog_path to "/blog" your full blog URL would be
#  "http://www.yoursite.com/~ryan/blog"
#  Leave blank "" to set to the root of site_url
blog.path = "/blog"

## blog_name -- Your Blog's name.
# This is used repeatedly in default blog templates
blog.name = "tanarky.com"

## blog_description -- A short one line description of the blog
# used in the RSS/Atom feeds.
blog.description = "tanarky website"

## blog_timezone -- the timezone that you normally write your blog posts from
blog.timezone = "Asia/Tokyo"

blog.disqus.enabled = True
blog.disqus.name    = "tanarky"

## 背景白
#filters.syntax_highlight.style   = "murphy"
## 背景黒
filters.syntax_highlight.style   = "monokai"
#filters.syntax_highlight.css_dir = "/css"
filters.syntax_highlight.preload_styles = ["monokai"]
css_dir = "/css"

import logging
import subprocess
def post_build():
    if os.path.isdir("_site"):
        subprocess.call("mkdir -p css js img _site/css _site/js _site/img", shell=True)
        subprocess.call("cp css/* _site/css/", shell=True)
        subprocess.call("cp js/*  _site/js/",  shell=True)
        subprocess.call("cp img/*  _site/img/",shell=True)
        subprocess.call("rm -rf ../blog",      shell=True)
        subprocess.call("cp -pr _site/* ../",  shell=True)
    else:
        logging.error("build failed. because _site dir not exists.")
