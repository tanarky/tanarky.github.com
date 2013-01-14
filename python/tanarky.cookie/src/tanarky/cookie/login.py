# coding: utf-8
import urllib, urlparse, random, logging

import tanarky.util.caesar
import tanarky.util.sig

class Login(object):
    version = '1'

    def __init__(self, secret, expire=60*60*24*14):
        self.secret = secret
        self.expire = expire

    def generate(self, key, additional={}, lang='en_US', intl='US'):
        rot = random.randrange(255)
        k = tanarky.util.caesar.encode(key, rot)

        a = tanarky.util.caesar.encode(urllib.urlencode(additional), rot)
        l = {'v': self.version,
             'k': k,
             'a': a,
             'r': hex(rot)[2:],
             'l': lang,
             'i': intl}

        return [urllib.urlencode(l),''];
        
if __name__ == '__main__':
    l = Login(secret='foo')
