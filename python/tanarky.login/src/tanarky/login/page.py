# coding: utf-8
import urllib, urlparse, random, logging, time

from tanarky.util.caesar import encode, decode, encode_hex, decode_hex, raw_encode, raw_decode
from tanarky.util.sig    import gen as sig_gen

from flask import Flask, request, render_template
from flaskext.babel import Babel, lazy_gettext, gettext, refresh
app = Flask(__name__)
# app.config.from_pyfile('mysettings.cfg')
babel = Babel(app)

@babel.localeselector
def get_locale():
    locale = request.accept_languages.best_match(['ja', 'ja_JP', 'en'])
    logging.debug("locale: %s" % locale)
    return locale

@app.route('/')
def hello_world():
    T = {'hello': gettext(u'hello world')}
    return render_template('index.html', T=T)

if __name__ == '__main__':
    logging.getLogger().setLevel(logging.DEBUG)
    app.run(debug=True, port=5000)
        
