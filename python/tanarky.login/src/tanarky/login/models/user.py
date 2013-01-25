# coding: utf-8
import urllib, urlparse, random, logging, time, binascii, sys, traceback

from tanarky.cookie.login import Login as CookieLogin

class User(object):
    def __init__(self, L=None, T=None):
        secret = 'zmVDRCilvXAcAe9R53IED3nLXlgaIuWw'
        expire = 10
        clogin = CookieLogin(secret=secret,
                             expire=expire)

        self.cookie_login = clogin
        self.status = 0
        self.id     = None
        self.email  = None

        try:
            login = clogin.decrypt(L, T)
            if login:
                if login.get('expired'):
                    self.status = 2
                else:
                    self.status = 1

                self.id    = login.get('key')
                self.email = login.get('additional',{}).get('m')
            logging.debug(login)
        except:
            self.status = 0
            self.id     = None
            self.email  = None
            logging.error(traceback.format_exc())

    def is_expired(self):
        ret = False
        if self.status == 2:
            ret = True
        return ret

    def login(self, email, password):

        if email == 'tanarky@gmail.com' and password == 'hoge':

            lt_key  = "%d" % (binascii.crc32(email) & 0xffffffff)
            lt_add  = {'m': email}
            lt_lang = 'ja_JP'
            lt_intl = 'JP'
            [L, T] = self.cookie_login.generate(key=lt_key,
                                                additional=lt_add,
                                                lang=lt_lang,
                                                intl=lt_intl)
            logging.debug("L: %s" % L)
            logging.debug("T: %s" % T)

            self.is_login = True
            self.id       = "123"
            self.email    = 'tanarky@yahoo.co.jp'
            return [L, T]
        return None

