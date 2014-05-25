---
categories: tips
date: 2014/05/25 15:00:00
title: Mac における zshのPATH設定
---

Mac環境(tmux含む)のPATHがおかしくなったので、メモ

.. code-block:: none

  % cat /etc/zprofile
  % cat /etc/zshenv
  # system-wide environment settings for zsh(1)
  if [ -x /usr/libexec/path_helper ]; then
     PATH=''
     eval `/usr/libexec/path_helper -s`
  fi
  source /etc/profile.d/rvm.sh
  % cat ~/.zlogin
  % cat ~/.zprofile
  % cat ~/.zshrc
  (略)
  export PATH=$PATH:$HOME/go/1.1.2/bin
  % echo $PATH
  /usr/local/rvm/gems/ruby-1.9.3-p392/bin:
  /usr/local/rvm/gems/ruby-1.9.3-p392@global/bin:
  /usr/local/rvm/rubies/ruby-1.9.3-p392/bin:
  /usr/local/rvm/bin:
  /opt/local/bin:
  /usr/bin:/bin:
  /usr/sbin:
  /sbin:
  /usr/local/bin:
  /Users/satoshi/go/1.1.2/bin
  % ls /etc/paths.d/
  % cat /etc/paths
  /opt/local/bin
  /usr/bin
  /bin
  /usr/sbin
  /sbin
  /usr/local/bin%

参考URL

- http://qiita.com/yuku_t/items/40bcc63bb8ad94f083f1
- http://pastak.hatenablog.com/entry/2014/02/21/025836
