---
categories: ubuntu,tips,python,install
date: 2011/11/09 14:00:00
title: Ubuntu 10.04 LTS server でpython環境をbuildoutで構築する
---

.. contents:: 目次

手順
=====================================

.. code:: none
  
  % sudo apt-get install zsh aptitude
  % sudo aptitude update
  % sudo aptitude install gcc zlib1g-dev libc6-dev libjpeg-dev -y

- 2012/01/22 追記

  - PILでjpegサポートさせるために、libjpeg-devを追加


