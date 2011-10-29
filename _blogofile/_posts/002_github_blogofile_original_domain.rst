---
categories: python,tips,ubuntu
date: 2011/10/29 20:00:00
title: githubとblogofileで独自ドメイン無料Blog環境構築
---

.. contents:: 目次

結論
=====================================================

いきなり結論。

`既存ブログサービスの問題に対する考察`_ で考えた理想のBlog環境は
以下のものを組み合わせることにより、ほぼ満足いく環境ができた。

1. `GitHub Pages`_ によるHTML公開+独自ドメイン設定
2. `Blogofile`_ による記事HTML+デザインの一括generate
3. `Bootstrap from twitter`_ によるデザイン設定の簡略化
4. `DISQUS`_ やその他ブログパーツによるブログのソーシャル化

今見ているこのBlogのソースコードは全て

https://github.com/tanarky/tanarky.github.com

に上げている。

以下、詳細。

Github PagesによるHTML公開+独自ドメイン設定
-----------------------------------------------------

GitHubでは、コードだけではなく、HTMLなどのドキュメントも
GitHubのサーバを用いて公開することができる。

静的なファイルであれば、HTMLやCSS/Javascriptなど公開可能。
画像ファイルも公開可能だが、無料ユーザの場合、容量制限が300Mなので、
画像ファイル置き場としてはあまり望ましくない。
PHPファイルなどサーバサイドでの動的処理は動かない。

この手段は、一部のオープンソースプロジェクトでよく利用されている。

設定な方法詳細は、 `GitHub Pages`_ を参照すれば詳しく書いてあるが
ユーザごとのページ設定手順をざっと説明すると、以下の通り。

1. GitHubのユーザ名(アカウント)を tanarky とする
2. tanarky.github.com というリポジトリを作成する
3. リポジトリ直下にindex.htmlという名前のHTMLファイルをコミットし、pushする
4. http://tanarky.github.com/ で公開したHTMLが見えるようになる

と、いたって簡単。

tanarky.github.com というドメイン名が気に入らなければ、
**独自ドメイン設定も可能** 。

valuedomainなどで取得済みのドメイン名が *example.com* だった場合、

*github.example.com* というサブドメインで公開したければ、

.. code:: none
  
  cname github pages.github.com.

サブドメインではなく、 *example.com* で公開したければ、

.. code:: none
  
  a @ 207.97.227.245

と、どちらかお好みのDNS設定をする。

次に、tanarky.github.comというリポジトリの直下に、 *CNAME* というファイル名で、
中身に公開したい独自ドメイン名を書く。

*example.com* で公開したければ、

.. code:: none
  
  example.com

と1行書いて保存すればOK。

これをgit pushして、DNSの設定が反映されれば設定完了。

GitHubを用いることで、無料のHTMLサーバと、
gitによるコード管理とバックアップ環境が、同時に無料で手に入ってしまった。


Blogofileを使った記事+デザイン構築
-----------------------------------------------------

`Blogofile`_ とは、markdown形式やrestructuredText形式のファイルから、
静的HTMLをgenerateして、ブログページを構築してくれるPythonで書かれたツールのこと。

1コマンドでカテゴリ分類やRSSなども一括でgenerateしてくれる。

インストール方法、の前に、まずはPython環境を整える必要があるので、
`Ubuntu11.10のPython開発環境を整備`_ を一読することをおすすめします。

綺麗なPython環境ができたところで、インストール。

.. code:: none

  % pip install blogofile
  % cd ~/github/tanarky.github.com
  % mkdir _blogofile
  % cd _blogofile
  % blogofile init simple_blog
  % blogofile build

これで完了。
ポイントとしては、ディレクトリ名を "_blogofile" と "_" から始まる名前にしておくこと。

GitHub Page経由では、"_" から始まるファイル名やディレクトリ名は見えなくなるという仕様を利用するため。

github経由でソースが見れるんだから意味ないじゃん、という言い分もあるが、
GitHub Page経由では公開する必要がないファイルなので、
公開したいファイルやディレクトリと明示的に区別するために、"_" から始まる名前にしておく。

buildが終わったら、blogofileには、 **Webサーバが同梱されている** ので、

.. code:: none
  
  % blogofile serve 10080
  Blogofile server started on 127.0.0.1:10080 ...

などとWebサーバを起動させれば、http://localhost:10080/でサイトを確認することができる。

投稿は、_blogofile/_post/ 以下に、markdown形式やrst形式などでファイルを置いておけば、
build実行時に勝手にブログ記事にしてくれる。

自分はrst形式に慣れているので、rst形式で記事を書いている。


Bootstrap from twitterを使ったデザイン
-----------------------------------------------------

デザインを1から作るのは大変なので、使ったことがある jQuery UI を使おうか、と思ったが、
このブログでは、勉強がてら、 `Bootstrap from twitter`_ を使ってみた。

アイコンなどの画像は一切ついていないが、
レイアウトなど、非常に直感的にデザインをいじることができるので満足している。


DISQUSなどブログパーツを用いたソーシャル対応など
-----------------------------------------------------

動的な処理は一切動かないので、各種ブログパーツに委ねないと、なんとも寂しいブログになるので、
好みのものを配置する。

個人的に、あまりブログパーツを置き過ぎると表示が重くなるのと、
見た目もごちゃごちゃするので、おいたのは以下のものだけ。

- `DISQUS`_
- `twitter公式 tweet数表示widget`_

`DISQUS`_ は、Javascriptで動く、コメントやトラックバック機能を実現できるモジュールで、
このブログの一番下にも貼ってあるブログパーツ。

ログインしないとコメントさせない設定、など非常に機能が豊富で、
何より静的なHTMLの中でこういう機能が実現できるのが嬉しい。

諦めた機能
=====================================================

静的なHTMLのブログ、ということでいくつか諦めた機能は以下。

- Smartphone用にページ表示を最適化して見せること
- 時限式の記事反映（明日の12時に自動で反映されるように設定する、など）
- 画像アップロード機能（画像はFlickrなどにまとめて置くようにする）


まとめ
=====================================================

長々と書いたが、上記のような構成のブログ環境は、アメリカなど海外ではやや浸透しつつある構成っぽい。
ぐぐると英語のページが色々ひっかかったので。

ただ、上記の設定内容を1つのページにまとめて書かれたものはなかったので、頑張って書いてみた次第。

GitHubにpushしなくても、上述の通り、Blogofileにはwebサーバも同梱されているので、
プライベートなブログとしてこっそり書くこともできるし、
個人ブログという用途だけではなく、プロジェクトページや企業ページでも使えると思うので、
興味を持った人は是非お試しください。

Blogofileの細かいカスタマイズや、SEO対策など、git branchの使い方など、
細かい点は色々他にもあるので、今後記事にしていく予定。

.. _`既存ブログサービスの問題に対する考察`: /blog/2011/10/29/003_problems_of_web_tool_based_blog_service
.. _`Ubuntu11.10のPython開発環境を整備`: /blog/2011/10/26/001_python_development_environment/
.. _`GitHub Pages`: http://pages.github.com/
.. _`Bootstrap from twitter`: http://twitter.github.com/bootstrap/
.. _`DISQUS`: http://disqus.com/
.. _`Blogofile`: http://www.blogofile.com/
.. _`twitter公式 tweet数表示widget`: http://twitter.com/about/resources/tweetbutton

