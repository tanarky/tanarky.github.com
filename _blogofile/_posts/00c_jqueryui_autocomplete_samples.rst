---
categories: javascript,jquery,jqueryui
date: 2012/02/11 21:00:00
title: jQuery UI autocomplete サンプル
---

.. contents:: 目次

jQuery UI の autocomplete ウィジェットについて
調査したので、その時のメモ

jquery version
  1.7.1

jquery UI version
  1.8.16

スクロールバー付きサンプル
======================================

銀行名か金融機関コードで検索して、
入力補完してくれるサンプルを書いた

- `jquery UI autocomplete スクロール付きサンプル`_
- `jquery UI autocomplete スクロール付きサンプル(ソースコード)`_

.. _`jquery UI autocomplete スクロール付きサンプル`: http://tanarky.com/samples/jqueryui/autocomplete/sample3.html

.. _`jquery UI autocomplete スクロール付きサンプル(ソースコード)`: https://github.com/tanarky/tanarky.github.com/blob/master/samples/jqueryui/autocomplete/sample3.html

ポイントは以下の通り

1. .ui-autocompleteクラスにmax-heightを指定することで、autocomplete部分のスクロールを実現
2. 候補がクリックされたときに、そのイベントを拾って、別フィールド2つにデータを補完
3. 別フィールドはreadonly属性で編集不可に
4. autocomplete optionにminLength=0を指定。入力がなくても、下キーで候補表示
5. suggestデータは、javascript内部にベタ書きで持っている。

  - データ構造は、配列
  - 配列の要素は、Hashで、valueというキーの値が検索対象となる
  - value以外は、任意のキーを指定可能


同一suggestデータサンプル
======================================

こちらも、銀行名か金融機関コードで検索して、
入力補完してくれるサンプル。

前のサンプルと違う点は、2つのフィールドに対して、同一のsuggestデータを使っている

- `jquery UI autocomplete 2つの検索フィールドサンプル`_
- `jquery UI autocomplete 2つの検索フィールドサンプル(ソースコード)`_

.. _`jquery UI autocomplete 2つの検索フィールドサンプル`: http://tanarky.com/samples/jqueryui/autocomplete/sample4.html

.. _`jquery UI autocomplete 2つの検索フィールドサンプル(ソースコード)`: https://github.com/tanarky/tanarky.github.com/blob/master/samples/jqueryui/autocomplete/sample4.html

ポイントは以下の通り

1. focusオプションで、候補にマウスオーバーした時点でデータを入れる(return false忘れずに)
2. 複数のフィールドに同一オプションでautocomplete登録

remote問い合わせsuggest
======================================

上記2つのサンプルは、挙動を理解しやすいようにするため、
サジェストするためのデータはコードに埋めたが、
remote API呼び出しも可能。

- `jquery UI autocomplete 公式ドキュメント demo(remote API呼び出し)`_

.. _`jquery UI autocomplete 公式ドキュメント demo(remote API呼び出し)`: http://jqueryui.com/demos/autocomplete/#remote

上記のサンプルでは、jquery側空、search.phpというAPIを呼び出し、
APIがJSON形式のデータを返している。

APIは、GETのパラメータで"term"を受け取り、
それに基づくsuggestデータを返却している

http://jqueryui.com/demos/autocomplete/search.php?term=or

関連リンク
======================================

- `jquery UI autocomplete 公式ドキュメント demo`_

.. _`jquery UI autocomplete 公式ドキュメント demo`: http://jqueryui.com/demos/autocomplete/
