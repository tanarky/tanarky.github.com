---
categories: tips,ubuntu,install
date: 2012/01/02 14:00:00
title: PostfixでGmail経由メール送信環境構築 on Ubuntu
draft: False
---

.. contents:: 目次

環境構築手順
=====================================

AppEngineの開発環境で、メール送信機能を使うために
postfixを使ったgmail送信環境の構築を行ったので、メモ。

まずは、package install

.. code:: none
  
  % sudo aptitude install postfix libsasl2-modules

/etc/postfix/main.cf を編集

以下を追記

.. code:: none
  
  # tanarky added
  mydomain = tanarky.com
  myorigin = $myhostname
  relayhost = [smtp.gmail.com]:587
  smtp_use_tls = yes
  smtp_tls_CAfile = /etc/ssl/certs/ca-certificates.crt
  smtp_sasl_auth_enable = yes
  smtp_sasl_password_maps = hash:/etc/postfix/relay_password
  smtp_sasl_security_options = noanonymous
  smtp_sasl_tls_security_options = noanonymous
  smtp_sasl_mechanism_filter = plain

パスワードファイル作成

.. code:: none
  
  % sudo cat /etc/postfix/relay_password
  [smtp.gmail.com]:587 *(Googleアカウント)*@gmail.com:*(Googleアカウントパスワード)*
  % sudo postmap /etc/postfix/relay_password
  % ls -l /etc/postfix/relay_password*
  -rw-r--r-- 1 root root    48 2012-01-01 22:17 /etc/postfix/relay_password
  -rw-r--r-- 1 root root 12288 2012-01-01 22:17 /etc/postfix/relay_password.db
  % sudo rm /etc/postfix/relay_password 
  % ls -l /etc/postfix/relay_password*
  -rw-r--r-- 1 root root 12288 2012-01-01 22:17 /etc/postfix/relay_password.db

postfix restartしてテスト送信

.. code:: none
  
  % sudo /etc/init.d/postfix restart
  % sendmail -t ***
  To: ***
  From: ***
  Subject: hello
  
  world.
  
  .
  %

参考
================

- http://www.icoro.com/200908243988.html
- http://blog.tanarky.com/2010/09/centosgmail.html


