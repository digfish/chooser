#!/usr/bin/env python

import os

try:
    import setuptools
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()

from setuptools import setup

import distutils.command.build
import distutils.command.clean
import distutils.command.sdist

man_file = 'chooser.1'
man_src = 'chooser.rst'

def build_man_file(man_file):
    if not os.path.isfile(man_file):
        try:
            import docutils
        except:
            raise RuntimeError('docutils required to build man file')
        import docutils.core
        import docutils.writers.manpage
        w = docutils.writers.manpage.Writer()
        docutils.core.publish_file(source_path=man_src,
                                   destination_path=man_file, writer=w)


class build(distutils.command.build.build):
    def run(self):
        build_man_file(man_file)
        distutils.command.build.build.run(self)

class sdist(distutils.command.sdist.sdist):
    def run(self):
        build_man_file(man_file)
        distutils.command.sdist.sdist.run(self)

class clean(distutils.command.clean.clean):
    def run(self):
        distutils.command.clean.clean.run(self)
        if os.path.isfile(man_file):
            os.unlink(man_file)

NAME =                'chooser'
VERSION =             '0.3.3'
AUTHOR =              'Lev Givon'
AUTHOR_EMAIL =        'lev@columbia.edu'
URL =                 'https://github.com/lebedov/chooser/'
DESCRIPTION =         'Choose browser when opening a URI'
LONG_DESCRIPTION =    DESCRIPTION
LICENSE =             'BSD'
CLASSIFIERS = [
    'Development Status :: 3 - Alpha',
    'Environment :: X11 Applications',
    'Intended Audience :: End Users/Desktop',
    'License :: OSI Approved :: BSD License',
    'Operating System :: POSIX',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.7',
    'Topic :: Desktop Environment',
    'Topic :: Internet :: WWW/HTTP'
    ]
DATA_FILES = [('man/man1', [man_file])]
CMDCLASS = {'build': build,
            'clean': clean,
            'sdist': sdist}

if __name__ == "__main__":
    setup(
        name = NAME,
        version = VERSION,
        author = AUTHOR,
        author_email = AUTHOR_EMAIL,
        license = LICENSE,
        classifiers = CLASSIFIERS,
        description = DESCRIPTION,
        long_description = LONG_DESCRIPTION,
        url = URL,
        scripts = ['chooser'],
        install_requires = ['pyxdg',
                            'wxPython'],
        data_files = DATA_FILES,
        cmdclass = CMDCLASS)
