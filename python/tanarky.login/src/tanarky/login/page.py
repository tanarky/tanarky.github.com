# coding: utf-8
import urllib, urlparse, random, logging, time, binascii

from tanarky.util.caesar  import encode, decode, encode_hex
from tanarky.util.caesar  import decode_hex, raw_encode, raw_decode
from tanarky.util.sig     import gen as sig_gen
from tanarky.cookie.login import Login

from flask import Flask, request, render_template, redirect, url_for, flash
from flaskext.babel import Babel, lazy_gettext, gettext, refresh
app = Flask(__name__)
app.secret_key = 'tanarky'
# app.config.from_pyfile('mysettings.cfg')
babel = Babel(app)

@babel.localeselector
def get_locale():
    locale = request.accept_languages.best_match(['ja', 'ja_JP', 'en'])
    logging.debug("locale: %s" % locale)
    return locale

@app.route('/')
def index():
    T = {'hello': gettext(u'hello world')}
    return render_template('index.html', T=T)

@app.route('/login', methods=['GET', 'POST'])
def login():
    T = {'hello': gettext(u'hello world')}
    if request.method == 'POST':
        if request.form.get('email') == 'tanarky@gmail.com' and \
                request.form.get('password') == 'hoge':

            secret = 'zmVDRCilvXAcAe9R53IED3nLXlgaIuWw'
            expire = 10
            login  = Login(secret=secret,
                             expire=expire)

            lt_key  = "%d" % (binascii.crc32(request.form.get('email')) & 0xffffffff)
            lt_add  = {'m': request.form.get('email')}
            lt_lang = 'ja_JP'
            lt_intl = 'JP'
            [L, T] = login.generate(key=lt_key,
                                    additional=lt_add,
                                    lang=lt_lang,
                                    intl=lt_intl)
            logging.debug("L: %s" % L)
            logging.debug("T: %s" % T)
            flash('You were successfully logged in', 'success')
            next = request.args.get('next', url_for('index'))
            return redirect(next)
        else:
            flash('invalid login id or password', 'error')
            return redirect(url_for('login'))

    return render_template('login.html', T=T)

@app.route('/logout')
def logout():
    flash('logout success', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    logging.getLogger().setLevel(logging.DEBUG)
    app.run(debug=True, port=5000)
        
