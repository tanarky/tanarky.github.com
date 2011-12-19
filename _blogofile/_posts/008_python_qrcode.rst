---
categories: tips,python
date: 2011/12/19 14:00:00
title: PythonでQRコード生成
draft: False
---

.. contents:: 目次

環境構築手順
=====================================

libqrencodeのpython bindingによるQRコード生成

まずはinstall

.. code:: none
  
  % sudo aptitude install libqrencode3 libqrencode-dev
  % pip install qrencode

動作確認
=====================================

サンプルコード

.. code:: python
  
  import qrencode
  
  e = Encoder()
  image = e.encode('http://tanarky.com/', { 'width': 100 })
  image.save("/tmp/qrcode.png")

リンク
=====================================

- https://github.com/bitly/pyqrencode
