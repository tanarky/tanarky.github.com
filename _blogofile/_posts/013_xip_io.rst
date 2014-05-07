---
categories: tips
date: 2014/05/06 15:00:00
title: wildcard DNS for any IP address なサービスの xip.io を使ってみた
---

http://xio.io/ provides wildcard DNS for any IP address.

というわけで使ってみたメモ。

任意のportで受け付けるには、以下の様に一旦80番ポートで受けてからサブドメインで再度proxyするようにnginxを設定した

.. code-block:: none
  
  http://port8000.10.0.0.1.xip.io/ -> nginx(port 80) on 10.0.0.1 -> (proxy to 8000) -> http://127.0.0.1:8000/
  http://port8080.10.0.0.1.xip.io/ -> nginx(port 80) on 10.0.0.1 -> (proxy to 8080) -> http://127.0.0.1:8080/


自分のサーバに置くnginx confのサンプルは以下の通り。

.. code-block:: nginx
  
  server {
    listen 80;
  
    server_name "~^port(\d+)\.([^.]+\.[^.]+)\.((?:\d{1,3}\.){3}\d{1,3})\.xip\.io$";
  
    access_log  /var/log/nginx/dev.access.log;
  
    location / {
      proxy_set_header host $host;
      proxy_set_header x-real-ip $remote_addr;
      proxy_set_header x-forwarded-for $proxy_add_x_forwarded_for;
      proxy_pass http://127.0.0.1:$1;
    }
  }
