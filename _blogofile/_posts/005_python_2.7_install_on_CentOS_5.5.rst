---
categories: centos,tips,install,python
date: 2011/11/16 00:00:00
title: CentOS 5.5 に python2.7環境を構築
---

.. contents:: 目次

手順
========================================

CentOS 5.5に入っているpythonのバージョンは、2.4.3と超古いので、
2.7.2の環境を構築したときのメモ

一度2.7.2の環境を作れば、
あとはvirtualenvで環境を切り分ければいいので、
それまでの手順

.. code:: none
  
  % mkdir ~/src_python2.7
  % cd ~/src_python2.7
  % wget http://www.python.org/ftp/python/2.7.2/Python-2.7.2.tar.bz2
  % tar -xvjf Python-2.7.2.tar.bz2
  % cd Python-2.7.2
  % ./configure --enable-shared --with-threads
  % make
  % sudo make install
  % sudo ln -s /opt/python2.7/lib/libpython2.7.so.1.0 /lib64/libpython2.7.so.1.0
  % sudo ln -s /usr/local/bin/python2.7 /usr/bin/python2.7
  % mkdir ~/src_setuptools
  % cd ~/src_setuptools
  % wget http://pypi.python.org/packages/2.7/s/setuptools/setuptools-0.6c11-py2.7.egg
  % sudo yum install zlib-devel.x86_64
  % chmod +x setuptools-0.6c11-py2.7.egg
  % sudo ./setuptools-0.6c11-py2.7.egg
  % sudo easy_install pip
  % sudo pip install virtualenv virtualenvwrapper

virtualenv環境構築。
後で配布することを想定して、デフォルトの".virtualenvs"から"virtualenv"に変更する。

以下を.zshrcに追加

.. code:: none
  
  export WORKON_HOME=$HOME/virtualenvs
  source /usr/local/bin/virtualenvwrapper.sh

環境を構築

.. code:: none
  
  % mkvirtualenv -p /usr/local/bin/python2.7 2.7.2
  % workon 2.7.2

とりあえずうまく環境が構築できたが、
複数台環境にpython環境を丸ごと配布したいので、
次はその方法を調べてみる。

参考
========================================

- `CentOS5.6 に Python2.7 + virtualenv で開発環境を整える | Pythonコード帳`_

.. _`CentOS5.6 に Python2.7 + virtualenv で開発環境を整える | Pythonコード帳`: http://python.codenote.net/python/centos5-6%E3%81%ABpython2-7%E3%81%A8virtualenv%E3%81%A7%E9%96%8B%E7%99%BA%E7%92%B0%E5%A2%83%E3%82%92%E6%95%B4%E3%81%88%E3%82%8B.html

