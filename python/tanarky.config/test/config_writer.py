# coding: utf-8

import logging, sys, subprocess
import tanarky.config

confname="config"

def update(p, path, sec, key, val):
    logging.debug(p.read(confname, filepath))
    logging.debug(p.set( confname, sec, key, val))
    logging.debug(p.save(confname, filepath))

def cleanup(p, filepath):
    logging.debug(p.read(confname))
    logging.debug(p.save(confname, filepath))

def add_section(p, filepath, sec):
    logging.debug(p.read(confname, filepath))
    if not p.parsers[confname].has_section(sec):
        logging.debug(p.parsers[confname].add_section(confname, sec))
    logging.debug(p.save(confname, filepath))

def remove_section(p, filepath, sec):
    logging.debug(p.read(confname, filepath))
    if p.parsers[confname].has_section(sec):
        logging.debug(p.parsers[confname].remove_section(confname, sec))
    logging.debug(p.save(confname, filepath))

if __name__ == '__main__':
    logging.getLogger().setLevel(logging.DEBUG)
    p = tanarky.config.Parser()
    if sys.argv[1] == 'update':
        update(p, sys.argv[2], sys.argv[3], sys.argv[4])
    elif sys.argv[1] == 'add_section':
        add_section(p, sys.argv[2], sys.argv[3])
    elif sys.argv[1] == 'remove_section':
        remove_section(p, sys.argv[2], sys.argv[3])
    elif sys.argv[1] == 'cleanup':
        create(p, sys.argv[2])
    elif sys.argv[1] == 'test':
        subprocess.call(['echo', '"ok"'])

