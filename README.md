# BROKEN

**It seems this idea is fundamentally broken, because flex & bison hardcode all
kinds of paths in their executables, and thus their install dir is not
relocatable, which is necessary for a wheel install in a virtualenv to work.**


# flex + bison wrapper

[![PyPi](https://badgen.net/pypi/v/flex-bison)](https://pypi.org/project/flex-bison/)

This is just a simple wrapper around the GNU Flex lexical analyzer generator
and GNU Bison parser generator. Installing the Python module will place their
executables in `<python-prefix>/bin`. This was made for projects that depend on
Flex and Bison as part of their documentation build process and want to build
on ReadTheDocs: they only support Python dependencies, and building from source
each time eats away at their build time limit.

**Running setup.py on your machine directly is unlikely to work, as some of the
build logic is in the Dockerfile.** To build, do the following:

 - Run `release.sh`. This will build the Python wheel in a manylinux docker
   container and stick it in `dist/*.whl`.
 - Install the wheel locally. Note that if you have a version of flex/bison
   already installed through your package manager, it might break these if your
   python prefix is the same!
 - Make sure that the flex and bison executables are installed with the wheel.
