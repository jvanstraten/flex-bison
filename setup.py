#!/usr/bin/env python3

import os, platform, shutil, sys, subprocess, glob
from distutils.command.bdist import bdist as _bdist
from distutils.command.sdist import sdist as _sdist
from distutils.command.build import build as _build
from distutils.command.clean import clean as _clean
from setuptools.command.egg_info import egg_info as _egg_info
import distutils.cmd
import distutils.log
from setuptools import setup, Extension, find_packages
from wheel.bdist_wheel import bdist_wheel as _bdist_wheel

target_dir = os.getcwd() + "/target"
py_target_dir = target_dir + "/python"
include_dir = target_dir + "/include"
cmake_build_dir = target_dir + "/build"
prefix_dir = target_dir + "/prefix"
build_dir = py_target_dir + "/build"
dist_dir = py_target_dir + "/dist"

def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as f:
        return f.read()

class clean(_clean):
    def run(self):
        _clean.run(self)
        shutil.rmtree(target_dir)

class build(_build):
    def initialize_options(self):
        _build.initialize_options(self)
        self.build_base = build_dir

    def run(self):
        _build.run(self)

class bdist_wheel(_bdist_wheel):
    def finalize_options(self):
        _bdist_wheel.finalize_options(self)
        self.root_is_pure = False

    def get_tag(self):
        python, abi, plat = _bdist_wheel.get_tag(self)
        python, abi = 'py3', 'none'
        return python, abi, plat

class bdist(_bdist):
    def finalize_options(self):
        _bdist.finalize_options(self)
        self.dist_dir = dist_dir

class sdist(_sdist):
    def finalize_options(self):
        _sdist.finalize_options(self)
        self.dist_dir = dist_dir

class egg_info(_egg_info):
    def initialize_options(self):
        _egg_info.initialize_options(self)
        self.egg_base = py_target_dir

setup(
    name = 'flex-bison',
    version = '0.0.2',

    author = 'QuTech, Delft University of Technology',
    author_email = '',
    description = 'Wheel wrapper around GNU flex/bison for use on ReadTheDocs',
    license = "Apache-2.0",
    url = "https://github.com/QE-Lab/py-flex-bison-wrapper",
    project_urls = {
        "Source Code": "https://github.com/QE-Lab/py-flex-bison-wrapper",
    },

    long_description = read('README.md'),
    long_description_content_type = 'text/markdown',

    classifiers = [
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",

        "Operating System :: POSIX :: Linux",

        "Programming Language :: C",
        "Programming Language :: C++",

        "Topic :: Software Development :: Code Generators"
    ],

    data_files = [
        ('bin', [
            '/usr/local/bin/flex',
            '/usr/local/bin/bison',
        ]),
    ],

    packages = find_packages('python'),
    package_dir = {
        '': 'python',
    },

    cmdclass = {
        'bdist': bdist,
        'bdist_wheel': bdist_wheel,
        'build': build,
        'clean': clean,
        'egg_info': egg_info,
        'sdist': sdist,
    },

    setup_requires = [
        'plumbum',
    ],

    zip_safe = False,
)
