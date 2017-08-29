# -*- coding: utf-8 -*-
"""`murray` lives on `Github`_.
.. _github: https://www.github.com/wlonk/murray
"""
import os
import sys

from io import open
from setuptools import (
    setup,
    Command,
)
from shutil import rmtree

from murray import __version__


class PublishCommand(Command):
    """Support setup.py publish."""

    description = 'Build and publish the package.'
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print('\033[1m{0}\033[0m'.format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status('Removing previous builds…')
            rmtree(os.sep.join(('.', 'dist')))
        except FileNotFoundError:
            pass

        self.status('Building Source and Wheel (universal) distribution…')
        os.system(
            '{0} setup.py sdist bdist_wheel --universal'.format(sys.executable),
        )

        self.status('Uploading the package to PyPi via Twine…')
        os.system('twine upload dist/*')

        sys.exit()


setup(
    name='murray',
    version=__version__,
    url='https://github.com/wlonk/murray/',
    license='MIT',
    author='Kit La Touche',
    author_email='kit@transneptune.net',
    description='Murray theme for Sphinx',
    long_description=open('README.rst', encoding='utf-8').read(),
    zip_safe=False,
    packages=['murray'],
    package_data={'murray': [
        'theme.conf',
        '*.html',
        'static/favicon.ico',
        'static/css/*.css',
        'static/js/*.js',
        'static/js/vendor/*.js',
        'static/img/*.*',
    ]},
    include_package_data=True,
    # See
    # http://www.sphinx-doc.org/en/stable/theming.html
    #     #distribute-your-theme-as-a-python-package
    entry_points={
        'sphinx_themes': [
            'path = murray:template_path',
        ],
        'sphinx.html_themes': [
            'murray = murray',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Operating System :: OS Independent',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
    ],
    # $ setup.py publish support.
    cmdclass={
        'publish': PublishCommand,
    },
)
