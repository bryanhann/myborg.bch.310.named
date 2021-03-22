#!/usr/bin/env python3
import functools
from pathlib import Path
from constants import INDEX, HOME

def _memoize(func):
    #https://medium.com/@nkhaja/memoization-and-decorators-with-python-32f607439f84
    cache = func.cache = {}
    @functools.wraps(func)
    def memoized_func(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return memoized_func


def find(name):
    return indexDict().get(name,[])


def list():
    for key,vals in sorted(indexDict().items()):
        for named in vals:
            yield named

@_memoize
def indexDict () :
    with open(INDEX) as fd:
        lines = fd.readlines()
    lines = [line.strip() for line in lines]
    acc = {}
    for line in lines:
        named = Named(line)
        name = named.name()
        if not name in acc:
            acc[name] = []
        acc[name].append(named)
    return acc

def build ():
    with open(INDEX, 'w') as fd:
        for path in Path(HOME).glob('**'):
            if path.name == '.named':
                print(path)
                fd.write(str(path) + '\n')
    print('---')
    print( INDEX.read_text() )

class Named :
    def __init__( self, path ):
        self._named = Path(path)
    def __repr__( self ):
        return '%s : %s' % (self.name(), self.root())
    def root(self):
        return self.named().parent
    def named(self):
        return self._named
    def name(self):
        namefile = self.named()/'name.txt'
        if namefile.exists():
            return namefile.read_text().strip()
        else:
            return 'anon'

