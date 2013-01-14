from setuptools import setup, find_packages

setup(
    namespace_packages=['tanarky'],
    packages     = ['tanarky', 'tanarky.util'],
    package_dir  = {'':'src'},
    #package_data = {
    #    'eventregist': ['templates/*.html', 'static/*.css'],
    #},
    name        = 'tanarky.util',
    version     = '1.0',
    )
