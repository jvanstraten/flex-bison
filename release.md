# Release process

The release process is as follows:

 - Update the version number in `setup.py`.
 - Run `release.sh`. This will build the Python wheel in a manylinux docker
   container and stick it in `dist/*.whl`.
 - Install the wheel locally.
 - Make sure that the flex and bison executables are installed with the wheel.
 - Push the wheel to PyPI with twine:

```
python3 -m pip install --user --upgrade twine
python3 -m twine upload dist/*
```
