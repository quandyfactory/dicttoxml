from distutils.core import setup

version = '1.7.5'

with open('README.markdown') as readme:
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
    download_url = 'https://pypi.python.org/packages/source/d/dicttoxml/dicttoxml-%s.tar.gz?raw=true' % (version),
    platforms='Cross-platform',
    classifiers=[
      'Programming Language :: Python',
      'Programming Language :: Python :: 3'
    ],
)
