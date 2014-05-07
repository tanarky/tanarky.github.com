---
categories: vagrant,aws,tips
date: 2014/05/06 11:00:00
title: vagrant version up and plugin install
---

vagrant version up
-----------------------------------

vagrant 1.6.0 がリリースされたのでバージョンアップした

vagrant selfupdate などでバージョンアップしたかったが対応してなかった

version upには、dmgを落として再installする必要あり

vagrant plugin install
-----------------------------------

vagrantにはpluginで機能拡張できる

packerを調べていたら以下のpluginを発見したので、以下の手順でinstallした

https://github.com/mitchellh/vagrant-aws

::
  
  % vagrant plugin list
  % vagrant plugin install vagrant-aws
