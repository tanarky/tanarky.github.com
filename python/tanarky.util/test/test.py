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

    # cookie.login
    """
# cookie config
cookie_secret = 'zmVDRCilvXAcAe9R53IED3nLXlgaIuWw'
cookie_expire = 60

# cookie data
cookie_key    = 'somekeystr'
cookie_add    = {'m':'tanarky@yahoo.co.jp'}

# make object
cookie = tanarky.cookie(secret=cookie_secret,
                        expire=60)

# has cookie data
login = cookie.decrypt(L, T)

if loggin:
    logging.debug('key:      %s' % login.get('key'))
    logging.debug('version:  %s' % login.get('version'))
    logging.debug('is_login: %s' % login.get('is_login'))

else:
    logging.debug('guest')


# no cookie data
[L, T] = cookie.generate(key=cookie_key,
                         additional=cookie_add,
                         lang='ja_JP',
                         intl='JP')
    """
