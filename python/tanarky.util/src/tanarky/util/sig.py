# coding: utf-8

import hashlib
import tanarky.util.caesar

def gen(mes, seed='jjWeHNCpqnDkwlv6GRgbz2z1w5yunL6DKimEluQaW4k4j52gfubkb1PfoLyZE4Ug'):
    return hashlib.sha1(mes+seed).hexdigest()[-16:]

if __name__ == '__main__':
    import logging
    logging.getLogger().setLevel(logging.DEBUG)
    print gen('foo')
    print gen('bar')
