import sys


def long_compatibility():
    if sys.version > '3':
        return int
    else:
        return long
