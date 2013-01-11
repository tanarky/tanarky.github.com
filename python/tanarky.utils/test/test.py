# coding: utf-8

import logging
import tanarky.utils.sig

if __name__ == '__main__':
    logging.getLogger().setLevel(logging.DEBUG)
    logging.info(tanarky.utils.sig.gen())

