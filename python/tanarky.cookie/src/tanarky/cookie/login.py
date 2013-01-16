# coding: utf-8
import urllib, urlparse, random, logging, time

from tanarky.util.caesar import encode, decode, encode_hex, decode_hex, raw_encode, raw_decode
from tanarky.util.sig    import gen as sig_gen

class Login(object):
    version = '1'

    def __init__(self, secret, expire=60*60*24*14):
        self.secret = secret
        self.expire = expire

    def generate(self, key, additional={}, lang='en_US', intl='US', remote_addr=''):
        rot = random.randrange(255)
        k = encode(key, rot)

        a = encode(urllib.urlencode(additional), rot)
        l = {'v': self.version,
             'k': k,
             'a': a,
             'r': encode_hex(rot),
             'l': lang,
             'i': intl}

        # a sig
        # k sig
        # exp
        # exp sig
        # ip
        # ip sig
        ipaddr      = encode(remote_addr, rot)
        loggedin_at = encode(encode_hex(int(time.time())), rot)
        lifetime    = encode(encode_hex(self.expire), rot)
        t = {'i':  ipaddr,
             'l':  loggedin_at,
             'e':  lifetime,
             'sk': raw_encode(sig_gen(k, self.secret), rot),
             'sa': raw_encode(sig_gen(a, self.secret), rot),
             'si': raw_encode(sig_gen(ipaddr, self.secret), rot),
             'se': raw_encode(sig_gen(lifetime, self.secret), rot),
             'sl': raw_encode(sig_gen(loggedin_at, self.secret), rot)}

        return [urllib.urlencode(l), urllib.urlencode(t)];


    def decrypt(self, L=None, T=None):
        try:
            l   = dict(urlparse.parse_qsl(L))
            t   = dict(urlparse.parse_qsl(T))

            if l.get('v') != '1':
                return None

            rot = decode_hex(l.get('r'))
            logging.debug(rot)
            k   = decode(l.get('k'), rot)
            a   = dict(urlparse.parse_qsl(decode(l.get('a'), rot)))

            ip  = decode(t.get('i', ''), rot)
            logging.debug(ip)

            loggedin_at = decode_hex(decode(t.get('l'), rot))
            logging.debug(loggedin_at)

            lifetime = decode_hex(decode(t.get('e'), rot))
            logging.debug(lifetime)

            sigl = ['k', 'a']
            for ss in sigl:
                if raw_encode(sig_gen(l.get(ss), self.secret), rot) != t.get('s%s' % ss):
                    logging.debug('sig ng(%s)', ss)
                    return None

            sigt = ['e',]
            for ss in sigt:
                if raw_encode(sig_gen(t.get(ss), self.secret), rot) != t.get('s%s' % ss):
                    logging.debug('sig ng(%s)', ss)
                    return None

            ret = {'key': k,
                   'additinal': a,
                   'lang': l.get('l'),
                   'intl': l.get('i')}

            return ret
        except:
            return None
        
if __name__ == '__main__':
    l = Login(secret='foo')
