===============================
eventregist API 1.0
===============================

API version 1.0

本番環境セットアップ
===============================

初回だけの手順
-------------------------------

1. mng01:/usr/share/erapi を本番環境にrsync
2. 本番に、//etc/eventregist/token.ini を用意、中身はmng01にあるものをベースに、mysqlの設定を本番に変更
3. 以下のcronを仕込む(暫定対応)
   # EventRegist API
   * * * * * /usr/share/erapi/bin/supervisorctl pid erapi | sudo -u nobody xargs kill -s HUP
4. mng01:/etc/init.d/supervisord と mng01:/etc/supervisord.conf を本番に配布して、本番で sudo /etc/init.d/superivsord start
5. sudo /usr/share/erapi/bin/supervisorctl status で RUNNINGになっていることを確認

2回目以降の反映手順
-------------------------------

1. git のマスターブランチをcloneして、make install @mng01
2. mng01から本番にrsync
3. プロセス再起動(ただし、毎分の再起動cronが動いているので今は別にいらないかも


開発環境設定
===============================

1. python2.6 install
2. virtualenv install
3. mkvirtualenv -p /path/to/python2.6 er26
4. pip install -r requirements.txt

.. code-block:: none

  % sudo yum install --enablerepo=epel python26 python26-devel python26-distribute
  % sudo easy_install-2.6 pip
  % sudo pip-2.6 install virtualenv
  % sudo virtualenv-2.6 /usr/share/erapi --distribute --python=/usr/bin/python26
  % sudo chown -R app:app /usr/share/erapi
  % sudo mkdir /etc/eventregist/
  % vi ~/.netrc
  % cd && mkdir git && cd git && git clone https://mng01.eventregist.com/git/er.git
  % cd er/api/1.0
  % sudo ln -s `pwd`/token.ini /etc/eventregist/
  % source /usr/share/erapi/bin/activate
  % pip install -r requirements.txt
  % make install

  % /usr/share/erapi/bin/python /usr/share/erapi/lib/python2.6/site-packages/eventregist/api.py
  または
  % make server

  % /usr/share/erapi/bin/gunicorn eventregist.api:app -p /tmp/er.pid -b 0.0.0.0:23456

- mac 開発環境セットアップ手順

.. code-block:: none
  
  % sudo port selfupdate
  % sudo port install python27 python26 py27-virtualenv
  % sudo /opt/local/bin/virtualenv-2.7 /usr/share/erapi --distribute --python=/opt/local/bin/python2.6
  % sudo chown -R satoshi:staff /usr/share/erapi
  % sudo mkdir /etc/eventregist/
  % ln -s `pwd`/token.ini /etc/eventregist/
  % source /usr/share/erapi/bin/activate


mng01環境構築
===============================

初期設定
-------------------------------

1. python venv環境構築

通常配布
-------------------------------

1. install
2. restart ?

本番環境構築
===============================

初期設定
-------------------------------

1. python venv環境構築
2. ~/.netrc設定
3. pip install freeze

通常配布
-------------------------------

1. pip install https://mng01.eventregist.com/er/api/1.0/release/eventregist-1.0.tgz
2. restart

DB
===============================

    $query = OrderCoreTable::getInstance()->createQuery('oc')
      ->innerJoin("oc.Event e")
      ->innerJoin("oc.EventDate ed")
      ->where("oc.user_id = ?", $this->getUser()->getUser()->id)
      ;

mysql> select oc.event_id,event.name from order_core as oc inner join event on event.id = oc.event_id where oc.user_id=19;
mysql> select event_id,name,price from ticket where event_id = 55;
mysql> select distinct(oc.event_id),event.name from order_core as oc inner join event on oc.event_id = event.id where oc.user_id=19;

API IF
===============================

getMyEvent
-------------------------------

- my event structure

- input

  - userid
  - (eventid)
  - (limit)
  - (offset)

- my event and ticket structure

- orders

.. code-block:: none
  
  { orders: [
     {...},
     {...},
     {
       id: "",
       event: {
         "id":"...",
         "name":"...",
         "code":"...",
         "start":"yyyy/mm/dd HH:MM:SS+0900",
         "end":"yyyy/mm/dd HH:MM:SS+0900",
         "status": 1,
         "place":{
           "name":"",
           "geo": {"lat":"123.111", "lon":"120.001"}
         },
       },
       "ticket_count": 7
     }
  ]}

.. code-block:: none

  {
     event: {
       "id":"...",
       "name":"...",
       "code":"...",
       "start":"yyyy/mm/dd HH:MM:SS+0900",
       "end":"yyyy/mm/dd HH:MM:SS+0900",
       "status": 1,
       "place":{
         "name":"",
         "geo": {"lat":"123.111", "lon":"120.001"}
       },
     },
     tickets:[
       {..},
       {..},
       {
         "id": "...",
         "code": "...",
       },
     ]
  }



- apis

  - order/search
    select oc.id,oc.event_id,oc.event_date_id,oc.user_id,oc.uid,ev.name,ev.code,ed.start,ed.end,ot.id,ot.ticket_name,ot.quantity from order_core as oc left join event as ev on oc.event_id = ev.id left join event_date as ed on oc.event_date_id = ed.id left join order_ticket as ot on oc.id = ot.order_core_id where oc.user_id = 19;

select oc.id,oc.event_id,oc.event_date_id,oc.user_id,oc.uid,ev.name,ev.code,ed.start,ed.end from order_core as oc left join event as ev on oc.event_id = ev.id left join event_date as ed on oc.event_date_id = ed.id where oc.user_id = 19;
してから
select sum(quantity) from order_ticket where order_core_id = 8906;

  - ticket/search
    select oc.id,oc.event_id,oc.event_date_id,ot.id,ot.ticket_name,at.checkin_key from order_core as oc left join order_ticket as ot on oc.id = ot.order_core_id right join attendee as at on ot.id = at.order_ticket_id where oc.user_id = 19 and oc.event_id = 1001;

地図表示
select ev.id,ev.name,up.name,up.googlemap_marker_lat,up.googlemap_marker_lng from event as ev left join user_place as up on ev.user_place_id = up.id where ev.id = 1001; 

order_core -> event = 1 -> 1
order_core -> event_date = 1 -> 1

order_core -> order_ticket = 1 -> many
order_ticket -> attendee = 1 -> many

MTG
-------------------

- order_search, ticket_search

  - APIの名前、売主か買い主か

- uidに変更
- status isLive() ?
- qr code file path -> ?





