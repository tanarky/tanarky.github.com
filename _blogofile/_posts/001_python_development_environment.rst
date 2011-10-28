---
categories: python,tips,ubuntu
date: 2011/10/26 15:22:00
title: Ubuntu11.10のPython開発環境を整備
---

.. contents:: 目次

背景
========================================

Google AppEngineで使い始めたのをきっかけにPythonにハマっている。
ハマった理由は以下の通り。

- 標準で備わってる機能が多い(CSV parserなど)
- Cのライブラリ連携が楽そう(ctypesなど)
- PyPI(PerlにおけるCPAN)パッケージが充実している
- など

ただ、パッケージが充実しているのはいいが、
野良CPANパッケージをinstallすると環境が汚れたり、
ちょっとお試しでinstallしたい場合に躊躇してしまう(Perlも同様)

pythonの場合、virtualenvを使えば、pythonのバージョン違いも含めて、
複数のpython環境を自分のHOMEディレクトリ以下で簡単に管理できるので、
その設定手順をまとめる


インストール手順
========================================

.. code:: none
  
  % sudo aptitude install python-virtualenv virtualwrapper
  % sudo aptitude install python3.2 python3.2-dev
  % mkvirtualenv -p /usr/bin/python2.7 2.7.2
  % mkvirtualenv -p /usr/bin/python3.2 3.2.2

パッケージをinstallできたら、
以下を.zshrcに追加

.. code:: none
  
  [ -f $HOME/.pythonbrew/etc/bashrc ] && source $HOME/.pythonbrew/etc/bashrc
  [ -f /etc/bash_completion.d/virtualenvwrapper ] && source /etc/bash_completion.d/virtualenvwrapper
  workon 2.7.2

これで準備は完了

後はterminal上で、"workon 2.7.2" や "workon 3.2.2" などと打てば
(python versionが異なる)環境を瞬時に切り替えられる

これで環境ごとにパッケージを完全に別で管理できるので、
とりあえずインストールして使ってみるsandbox環境として別に1つ用意するのも、あり。
