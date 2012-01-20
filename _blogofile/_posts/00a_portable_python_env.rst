---
categories: python,tips,install
date: 2012/01/20 14:00:00
title: (できるだけ)ポータブルなPython開発環境
---

.. contents:: 目次

背景
========================================

せっかくLLをさわっているので、

- OS依存が少ない
- 複数versionの環境の混在
- 構築の簡単さ
- 本番環境でも使える性能
- 環境をコピーできる

というPython環境が欲しくて、色々考えてる

buildoutとvirtualenvを用いた1つの解
=========================================

以下のようなことを考えた

- コンパイルが必要なライブラリ(Python自体も含む)をbuildoutでビルドする

  - Python
  - zlib
  - Graphviz
  - 画像系パッケージ?
  - (yum/aptitudeでもいいが、後々環境が混在できなくなるリスク)

- buldoutでbuildしたpythonを指定して、virtualenv環境を構築する
- PyPIパッケージは、virtualenvにinstallする
- サービスはvirtualenv環境ごとに分ける

  - サービスごとにpythonのバージョンをわけるためにBuildするのは大変
  - サービスごとにライブラリのバージョンが競合する可能性はあるので
    その時はbuildout環境を増やす

- 自分で書いたコードは、githubや自前distサーバなどにパッケージとしておいておく
- 環境から、distサーバ指定でpip installしてdeploy


参考手順
------------------

1. まずは、buildoutでOS依存しない場所にPythonと
   依存するライブラリなどをビルド

.. code:: none
  
  % mkdir /tmp/py27
  % cd /tmp/py27
  % (buildout.cfg + bootstrap.pyを用意)
  % cat buildout.cfg
  [buildout]
  python = python
  parts =
      python
      env
  
  [python]
  recipe = zc.recipe.cmmi
  url = http://www.python.org/ftp/python/2.7.2/Python-2.7.2.tgz
  executable = ${buildout:parts-directory}/python/bin/python2.7
  environment =
      LDFLAGS=-Wl,-rpath,${buildout:parts-directory}/python/lib
  extra_options =
      --enable-unicode=ucs4
      --enable-shared
      --with-threads
  
  [env]
  recipe = zc.recipe.egg
  eggs =
       virtualenv
       virtualenvwrapper
  
  interpreter = python
  
  % python bootstrap.py
  % bin/buildout

2. 1.で構築したpythonを使って、virtualenv環境を作る

.. code:: none
  
  % export WORKON_HOME=/tmp/virtualenvs
  % export VIRTUALENVWRAPPER_HOOK_DIR=/tmp/virtualenvs
  % export VIRTUALENVWRAPPER_LOG_DIR=/tmp/virtualenvs
  ## FIXME: クリーンな環境でうまくいくか?
  % mkvirtualenv -p /tmp/py27/parts/python/bin/python testenv
  % /tmp/virtualenvs/testenv/bin/pip install Flask
  % /tmp/virtualenvs/testenv/bin/pip install gunicorn
  % /tmp/virtualenvs/testenv/bin/pip install supervisor

3. 開発

.. code:: none
  
  % cat myserver.py
  
  from flask import Flask
  
  app = Flask(__name__)
  
  @app.route('/')
  def index():
      return "<h1>hello!Yes!</h1>"
  
  if __name__ == '__main__':
      app.run(debug=True)
  % /tmp/virtualenvs/testenv/bin/python myserver.py
     * Running on http://127.0.0.1:5000/
     * Restarting with reloader

4. インストール

cpでinstallしないほうがいい(暫定手順)

.. code:: none
  
  % sudo mkdir /tmp/virtualenvs/testenv/lib/python2.7/site-packages/mypj
  % touch /tmp/virtualenvs/testenv/lib/python2.7/site-packages/mypj/__init__.py
  % sudo cp myserver.py /tmp/virtualenvs/testenv/lib/python2.7/site-packages/mypj/

5. gunicornで本番プロセス起動

本当はdaemonモード

.. code:: none
  
  % /tmp/virtualenvs/testenv/bin/gunicorn mypj.myserver:app

まとめ など
==================================

- gunicornが起動するところまで確認できたので、supervisorで監視体制を整えたい
- 古めのCentOSでも動くか?
- zlib/graphvizなどのライブラリ系もbuildoutに組み込みたい





