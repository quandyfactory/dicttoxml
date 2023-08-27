from distutils.core import setup

version = '1.7.16'

with open('README.md') as readme:
    long_description = readme.read()

setup(
    name = 'dicttoxml',
    version = version,
    description = 'Converts a Python dictionary or other native data type into a valid XML string. ',
    long_description = long_description,
    author = 'Ryan McGreal',
    author_email = 'ryan@quandyfactory.com',
    license = 'GPL-2.0-only',
    url = 'https://github.com/quandyfactory/dicttoxml',
    py_modules = ['dicttoxml'],
    platforms='Cross-platform',
    python_requires=">=3.6",
)
