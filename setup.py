from distutils.core import setup

version = '1.5.6'

with open('README.markdown') as readme:
    long_description = readme.read()

setup(
    name = 'dicttoxml',
    version = version,
    description = 'Converts a Python dictionary or other native data type into a valid XML string. ',
    long_description = long_description,
    author = 'Ryan McGreal',
    author_email = 'ryan@quandyfactory.com',
    license = 'LICENCE.txt',
    url = 'https://github.com/quandyfactory/dicttoxml',
    py_modules = ['dicttoxml'],
    download_url = 'https://github.com/quandyfactory/dicttoxml/blob/master/dist/dicttoxml-%s.tar.gz?raw=true' % (version),
    platforms='Cross-platform',
    classifiers=[
      'Programming Language :: Python',
      'Programming Language :: Python :: 3'
    ],
)
