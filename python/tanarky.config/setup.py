from setuptools import setup, find_packages

setup(
    namespace_packages=['tanarky'],
    packages     = ['tanarky', 'tanarky.config'],
    package_dir  = {'':'src'},
    name        = 'tanarky.config',
    version     = '1.0',
    )
