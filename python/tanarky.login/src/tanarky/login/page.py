# coding: utf-8
import urllib, urlparse, random, logging, time, binascii

from flask import Flask, request, render_template, redirect, url_for, flash
from flaskext.babel import Babel, lazy_gettext, gettext, refresh
app = Flask(__name__)
app.secret_key = 'tanarky'
# app.config.from_pyfile('mysettings.cfg')
babel = Babel(app)

from models.user import User

@babel.localeselector
def get_locale():
    locale = request.accept_languages.best_match(['ja', 'ja_JP', 'en'])
    logging.debug("locale: %s" % locale)
    return locale

def init_page(T={}):
    T['user'] = User(request.cookies.get('L'),
                     request.cookies.get('T'))
    return T

@app.route('/')
def index():
    T = init_page()
    logging.debug(T['user'].id)
    logging.debug(T['user'].email)
    T['hello'] = gettext(u'hello world')
    return render_template('index.html', T=T)

@app.route('/login', methods=['GET', 'POST'])
def login():
    T = {'hello': gettext(u'hello world')}
    if request.method == 'POST':
        u = User()
        cookies = u.login(request.form.get('email'),
                          request.form.get('password'))
        if cookies:
            flash('You were successfully logged in', 'success')
            next = request.args.get('next', url_for('index'))
            resp = app.make_response(redirect(next))
            resp.set_cookie('L', value=cookies[0])
            resp.set_cookie('T', value=cookies[1])
            return resp
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
        
