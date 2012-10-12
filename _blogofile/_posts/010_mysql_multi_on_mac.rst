---
categories: mysql,install,env
date: 2012/10/11 10:00:00
title: mysql_multiをmacにinstall
---

.. contents:: 目次

Macbookにて、mysql_multiで複数サーバを立てたので、その時のinstallメモ

目的は、dual master replication の failover動作確認をするため

install
======================================

Macにmysqlはinstall済みであることが前提

メモリを食うので、必要な時だけ起動するようにplistはunloadしておく

.. code-block:: none

  # 起動していたら停止  
  % sudo /opt/local/share/mysql5/mysql/mysql.server stop
  % sudo launchctl load -w /Library/LaunchDaemons/org.macports.mysql5.plist
  
  # ここに入っている + pathは通しておく
  % which mysql5
  /opt/local/bin/mysql5
  
  # エラーになるのでリンクを張っておく等
  % sudo ln -s /opt/local/bin/my_print_defaults5 /opt/local/bin/my_print_defaults
  % mkdir -p /Users/satoshi.tanaka/var/mysql1
  % mkdir -p /Users/satoshi.tanaka/var/mysql2
  % mkdir -p /Users/satoshi.tanaka/var/log
  
  # ~/.my.cnf を準備, user名やportなどは適当に変更すること
  % cat ~/.my.cnf
  [mysqld_multi]
  mysqld     = /opt/local/lib/mysql5/bin/mysqld_safe
  mysqladmin = /opt/local/lib/mysql5/bin/mysqladmin
  user       = root
  
  [mysqld1]
  server-id  = 1
  socket     = /tmp/mysql1.sock
  port       = 13306
  pid-file   = /tmp/mysql1.pid
  datadir    = /Users/satoshi.tanaka/var/mysql1
  language   = /opt/local/share/mysql5/mysql/english
  user       = satoshi.tanaka
  log        = /Users/satoshi.tanaka/var/log/mysqld1.log
  log-error  = /Users/satoshi.tanaka/var/log/mysqld1.error.log
  
  [mysqld2]
  server-id  = 2
  socket     = /tmp/mysql2.sock
  port       = 13307
  pid-file   = /tmp/mysql2.pid
  datadir    = /Users/satoshi.tanaka/var/mysql2
  language   = /opt/local/share/mysql5/mysql/english
  user       = satoshi.tanaka
  log        = /Users/satoshi.tanaka/var/log/mysqld2.log
  log-error  = /Users/satoshi.tanaka/var/log/mysqld2.error.log
  
  # datadirの準備
  % mysql_install_db5 --datadir=./var/mysql1/
  % mysql_install_db5 --datadir=./var/mysql2/
  
  # 起動して確認
  % /opt/local/bin/mysqld_multi5 start --log=/tmp/mysqld_multi.log         
  % /opt/local/bin/mysqld_multi5 report --log=/tmp/mysqld_multi.log
  Reporting MySQL servers
  MySQL server from group: mysqld1 is running
  MySQL server from group: mysqld2 is running
  % mysql5 -S /tmp/mysql2.sock                                     
  Welcome to the MySQL monitor.  Commands end with ; or \g.
  Your MySQL connection id is 3
  Server version: 5.1.63-log Source distribution
  
  Copyright (c) 2000, 2011, Oracle and/or its affiliates. All rights reserved.
  
  Oracle is a registered trademark of Oracle Corporation and/or its
  affiliates. Other names may be trademarks of their respective
  owners.
  
  Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.
  
  mysql> 
