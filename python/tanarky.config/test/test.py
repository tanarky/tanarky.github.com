# coding: utf-8

import logging, sys
import tanarky.config

if __name__ == '__main__':
    logging.getLogger().setLevel(logging.DEBUG)
    logging.debug(sys.argv[0])
    p = tanarky.config.Parser()
    logging.debug(p)
    p = tanarky.config.Parser()
    logging.debug(p)
    p = tanarky.config.Parser()
    logging.debug(p)
    logging.debug(tanarky.config.Parser())
    logging.debug(tanarky.config.Parser())
    logging.debug(tanarky.config.Parser())
    logging.debug("file: %s" % sys.argv[1])

    logging.debug('-----')
    p_test = p.read('test', sys.argv[1])
    logging.debug(p_test)
    p_test = p.read('test', sys.argv[1])
    logging.debug(p_test)
    p_test = p.read('test', sys.argv[1])
    logging.debug(p_test)
    logging.debug(tanarky.config.Parser())

    # FIXME: こうやって書くと、別instanceになる
    logging.debug(tanarky.config.Parser().read('test', sys.argv[1]))
    logging.debug('-----')

    logging.debug(p.get('test', 'section1', 'key11', 'default0'))
    logging.debug(p.get('test', 'section2', 'key21', 'default0'))
    logging.debug(p.get('test', 'section1', 'key10', 'default0'))
    logging.debug(p.get('test0', 'section1', 'key10', 'default0'))
