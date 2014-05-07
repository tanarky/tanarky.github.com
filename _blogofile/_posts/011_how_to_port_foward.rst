---
categories: ssh,tips
date: 2014/05/06 10:00:00
title: ssh の Lオプション(port forward)
---

.. contents:: 目次

母艦Macから、Vagrant内にあるwebサーバを見るとき等に設定する

::
  
  ssh 192.168.100.10 -A -L 8080:localhost:8000
      ^^^^^^^^^^^^^^    ^^^^^^^^^^^^^^^^^^^^^^
      1                 2

1. vagrant hostのIP
2. local port:vagrant host name or IP:vagrant host port
   母艦で http://localhost:8080/ とすると http://vagrant_host:8000/ につながる
