"""
draft
-----

Draft is a small web app designed to make JavaScript library development and
debugging more fun.
"""
import sys
import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


if sys.argv[-1] == 'publish':
    os.system("python setup.py sdist upload")
    sys.exit()


setup(
    name='draft',
    version='0.1-dev',
    description='A web app that makes JavaScript library development fun',
    author='Ori Livneh',
    author_email='ori.livneh@gmail.com',
    license='MIT',
    long_description=__doc__,
    packages=['draft'],
    entry_points={
        'console_scripts': [
            'draft = draft:main',
        ],
    },
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
        'Topic :: Software Development'
    ),
    install_requires=('flask>=0.8'),
    url='https://github.com/atdt/draft',
    test_suite = 'draft.tests',
)
