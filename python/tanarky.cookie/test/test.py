# coding: utf-8

import logging
from tanarky.cookie.login import Login

if __name__ == '__main__':
    logging.getLogger().setLevel(logging.DEBUG)

    secret = 'zmVDRCilvXAcAe9R53IED3nLXlgaIuWw'
    expire = 60
    
    ltcookie = Login(secret=secret,
                     expire=expire)

    lt_key  = '1234567890'
    lt_add  = {'m':'tanarky@yahoo.co.jp'}
    lt_lang = 'ja_JP'
    lt_intl = 'JP'
    [L, T] = ltcookie.generate(key=lt_key,
                               additional=lt_add,
                               lang=lt_lang,
                               intl=lt_intl)

    logging.debug(L)
    logging.debug(T)

    logging.debug(ltcookie.decrypt(L, T))


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
