# coding: utf-8

import tanarky.utils.sig 
import tanarky.utils.caesar

if __name__ == '__main__':
    import logging, random
    logging.getLogger().setLevel(logging.DEBUG)

    # sig
    sig = tanarky.utils.sig.gen('foo')
    logging.info(sig)
    logging.info(tanarky.utils.caesar.encode(sig))
    logging.info(tanarky.utils.caesar.raw_encode(sig))

    # caesar
    enc = tanarky.utils.caesar.encode('foo')
    logging.info(enc)
    dec = tanarky.utils.caesar.decode(enc)
    logging.info(dec)
    n   = 120
    enc = tanarky.utils.caesar.encode('foo', n)
    logging.info(enc)
    dec = tanarky.utils.caesar.decode(enc, n)
    logging.info(dec)

    # cookie.login
    """
    cookie_secret = 'zmVDRCilvXAcAe9R53IED3nLXlgaIuWw'
    cookie_rot    = random.randrange(256)
    cookie_login  = 'tanarky@yahoo.co.jp'
    cookie_expsec = 60
    c = tanarky.utils.cookie.Login()
    c.get_name()
    c.is_login()

    secret=cookie_secret,
    expire=cookie_expsec,
    name=cookie_login,
    rot=cookie_rot,
    )

    cookie_l = '...'
    cookie_t = '...'
    tanarky.utils.login.is_login(l=l, t=t)
    """
