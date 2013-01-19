from setuptools import setup, find_packages

setup(
    namespace_packages=['tanarky'],
    packages     = ['tanarky', 'tanarky.login', 'tanarky.login.models'],
    package_dir  = {'':'src'},
    name        = 'tanarky.login',
    version     = '1.0',
    package_data = {
        'tanarky': ['login/translations/*/LC_MESSAGES/*.mo',
                    'login/templates/*.html',
                    'login/static/js/*.js',
#                    'login/static/img/*',
                    'login/static/css/*.css'],
        },
    )
