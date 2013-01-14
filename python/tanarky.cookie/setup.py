from setuptools import setup, find_packages

setup(
    packages     = find_packages('src'),
    package_dir  = {'':'src'},
    namespace_packages=['tanarky', 'tanarky.cookie'],
    name        = 'tanarky.cookie',
    version     = '1.0',
    )
