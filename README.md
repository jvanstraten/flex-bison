# flex + bison wrapper

[![PyPi](https://badgen.net/pypi/v/flex-bison)](https://pypi.org/project/flex-bison/)

This is just a simple wrapper around the GNU Flex lexical analyzer generator
and GNU Bison parser generator. Installing the Python module will place their
executables in `<python-prefix>/bin`. This was made for projects that depend on
Flex and Bison as part of their documentation build process and want to build
on ReadTheDocs: they only support Python dependencies, and building from source
each time eats away at their build time limit.

