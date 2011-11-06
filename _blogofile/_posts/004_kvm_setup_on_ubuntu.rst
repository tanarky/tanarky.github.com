---
categories: ubuntu,tips,kvm
date: 2011/11/09 14:00:00
title: kvmによる仮想環境構築 on Ubuntu 11.10
draft: True
---

.. contents:: 目次

手順
========================================

.. code: none
  
  /home/satoshi/% mkdir kvm
  /home/satoshi/% cd kvm
  /home/satoshi/kvm% sudo aptitude install qemu-kvm
  /home/satoshi/kvm% kvm-img create -f qcow2 ubuntu_10_10.img 10G
  Formatting 'ubuntu_10_10.img', fmt=qcow2 size=10737418240 encryption=off cluster_size=0
  /home/satoshi/kvm% ll
  合計 136
  -rw-r--r-- 1 satoshi satoshi 197120 2011-11-05 23:30 ubuntu_10_10.img

参考
========================================

http://research.sakura.ad.jp/2010/03/08/kvm-install/

結論
========================================

VMWareに比べて以下の点がデメリット

- 64bit guest os ubuntu 10.04 が動かなかった
- コマンドラインオプションが多すぎて覚えられない
- ネットワーク設定が面倒

  - Host -> Guest のsshが面倒
