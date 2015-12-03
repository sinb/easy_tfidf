from distutils.core import setup
from os import path
here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()
setup (
    name = 'easy_tfidf',
    version = '1.0.1',
    py_modules = ['easy_tfidf'],
    author = 'sinb',
    author_email = 'taa199@qq.com',
    description = 'An easy to use tool to compute TFIDF for several files, use folder name as input.',
    long_description=long_description,
    license='MIT',
)