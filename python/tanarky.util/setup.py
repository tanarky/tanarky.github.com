from setuptools import setup, find_packages

setup(
    packages     = find_packages('src'),
    package_dir  = {'':'src'},
    namespace_packages=['tanarky', 'tanarky.utils'],
    #package_data = {
    #    'eventregist': ['templates/*.html', 'static/*.css'],
    #},
    name        = 'tanarky.utils',
    version     = '1.0',
    )
