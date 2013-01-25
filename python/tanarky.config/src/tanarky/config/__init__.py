# coding: utf-8
import logging, os, ConfigParser, sys, traceback

class Parser(object):
    def __new__(clsObj, *args, **kwargs):
        logging.debug('called __new__')
        if not hasattr(clsObj, "__instance__"):
            clsObj.__instance__ = super(Parser, clsObj).__new__(clsObj, *args, **kwargs)
        return clsObj.__instance__
    
    def __init__(self, *args, **kwargs):
        self.parsers = {}
        logging.debug('called __init__')

    def save(self, name, path):
        try:
            with open(path, 'wb') as configfile:
                self.parsers.get(name).write(configfile)
            return True
        except:
            logging.debug(traceback.format_exc())
            return False

    def read(self, name, path=None, force_reload=False):
        logging.debug('called read: %s' % name)
        if self.parsers.get(name) and not force_reload:
            return self.parsers.get(name)

        logging.debug('parsers: %s' % self.parsers.get(name))
        logging.debug('read file: %s' % path)
        self.parsers[name] = ConfigParser.ConfigParser()
        if path:
            self.parsers[name].read(path)
        return self.parsers[name]

    def get(self, name, section, key, default=None):
        try:
            return self.parsers.get(name).get(section, key)
        except:
            return default

    def set(self, name, section, key, val):
        try:
            self.parsers.get(name).set(section, key, val)
            return True
        except:
            logging.debug(traceback.format_exc())
            return False

if __name__ == '__main__':
    logging.getLogger().setLevel(logging.DEBUG)
    #logging.debug(sys.argv[0])
    p = Parser()
