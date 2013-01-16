# coding: utf-8

import tanarky.util.sig 
import tanarky.util.caesar

if __name__ == '__main__':
    import logging, random, time
    logging.getLogger().setLevel(logging.DEBUG)

    teststr = 'foo'

    # sig
    sig = tanarky.util.sig.gen(teststr)
    logging.info(sig)
    logging.info(tanarky.util.caesar.encode(sig))
    logging.info(tanarky.util.caesar.raw_encode(sig))

    # caesar
    enc = tanarky.util.caesar.encode(teststr)
    logging.info(enc)
    dec = tanarky.util.caesar.decode(enc)
    logging.info(dec)
    n   = 120
    enc = tanarky.util.caesar.encode(teststr, n)
    logging.info(enc)
    dec = tanarky.util.caesar.decode(enc, n)
    logging.info(dec)

    # NOT normal pattern
    empty = ''
    enc = tanarky.util.caesar.raw_encode(empty, n)
    logging.info('empty raw endoded: (%s)' % enc)
    logging.info('empty sig gen: (%s)' % tanarky.util.sig.gen(empty))
    enc1 = tanarky.util.sig.gen(empty)
    enc2 = tanarky.util.caesar.raw_encode(enc1, n)
    logging.info('empty sig gen raw encoded1: (%s)' % enc1)
    logging.info('empty sig gen raw encoded2: (%s)' % enc2)
    dec1 = tanarky.util.caesar.raw_decode(enc2, n)
    logging.info('empty sig gen raw encoded -> decoded1: (%s)' % dec1)

