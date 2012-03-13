---
categories: javascript,install,env
date: 2012/03/12 14:00:00
title: Rhino/Node Javascript実行環境構築 on Macbook
---

.. contents:: 目次

Macbookにて、Javascript実行環境を整えたので、その際の手順履歴

Rhino
======================================

Rhino = Java実装のJavascript実行環境

その他の言語のJava実装は以下のものがある

.. code-block:: none
  
  Jython - port of Python.
  JRuby - port of Ruby.
  Rhino - port of ECMAScript.
  Clojure - Lisp dialect.
  Groovy - Scripting language for the JVM.
  Scala - object-oriented, functional language for the JVM.

Macにinstallするには、brew installで一発。

2012/03/12 時点でinstallされるversionは1.7R3

.. code-block:: none
  
  brew install rhino

実行するには以下のjarを指定する。-eでコードを直接渡す。

.. code-block:: none

  % java -jar /usr/local/Cellar/rhino/1.7R3/libexec/js.jar -e "print('hello world!');"
  java -jar /usr/local/Cellar/rhino/1.7R3/libexec/js.jar -e "print('hello worldjava -jar /usr/local/Cellar/rhino/1.7R3/libexec/js.jar');"
  hello worldjava -jar /usr/local/Cellar/rhino/1.7R3/libexec/js.jar
  %

インタラクティブシェルは以下の通りに実行できる

.. code-block:: none
  
  % java -jar /usr/local/Cellar/rhino/1.7R3/libexec/js.jar
  Rhino 1.7 release 3 2011 05 09
  js> print('hello world!');
  hello world!
  js> 
  
`Rhino <https://developer.mozilla.org/ja/Rhino>`_

Node
======================================

http://nodejs.org/

こちらもJavascript実行環境。実装はV8だったりSpiderMondkeyだったり。

同じく、brew installにて。

.. code-block:: none
  
  % brew install node

npmと単体テストフレームワークもついでにinstall

.. code-block:: none
  
  % git clone git://github.com/creationix/nvm.git ~/.nvm
  % nvm install v0.6.12
  % nvm alias default v0.6.12
  % source ~/.nvm/nvm.sh
  % curl http://npmjs.org/install.sh | sh
  % npm install nodeunit
  % ln -s $HOME/.npm/nodeunit/0.7.4/package/bin/nodeunit $HOME/bin/nodeunit

- `zsh on mac で nvm -> nvm_ls:17: no matches found: vdefault* 対処 <http://d.hatena.ne.jp/ToQoz/20120312/1331512182>`_
