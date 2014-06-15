---
categories: tips
date: 2014/06/15 10:00:00
title: Firefox on Mac に Flash Player をインストール
---

何故か Mac Book Pro の Firefox で Flash Player のインストールに失敗していたので対策した時のメモ

環境は以下のとおり

:Mac OS: X 10.9.3
:Firefox: 29.0.3
:インストールしようとしたFlash Player: 14.0.0.125

Flash Player Download Center ( http://get.adobe.com/flashplayer/ ) からだと、
インストール途中で失敗していた

結論から言うと、インストール途中で内部的に最新バージョンを取ってきて(ネットワーク?)インストールしている挙動っぽかったので、最初から Full version を落としてきてインストールしたら問題なく完了した。

Full version のリンク先は http://www.adobe.com/products/flashplayer/distribution3.html

参考URL
^^^^^^^^^^^^^^^^^^^^^^^

- https://support.mozilla.org/ja/questions/920187
- http://toshiohattori.blogspot.jp/2014/01/flash.html
- https://discussions.apple.com/message/21837402
- http://www.adobe.com/jp/software/flash/about/
