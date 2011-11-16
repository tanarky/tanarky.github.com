---
categories: elixir,tips,python
date: 2011/11/14 00:00:00
title: python Elixirを使ってJOIN
draft: True
---

.. contents:: 目次

python join
========================================

join連結

.. code:: python
  
  setup_all()
  for e, t in \
          session.query(Event, Ticket).\
          filter(Event.id==event_id).\
          filter(Event.id==Ticket.event_id).all():
      logging.error("event name: %s, ticket name: %s" % (e.name, t.name))
  session.close()

参考
========================================

- `オブジェクトリレーショナルマッパ　チュートリアル — SQLAlchemy 0.6.5 ドキュメント (和訳)`_

.. _`オブジェクトリレーショナルマッパ　チュートリアル — SQLAlchemy 0.6.5 ドキュメント (和訳)`: http://omake.accense.com/static/doc-ja/sqlalchemy/ormtutorial.htm#join

