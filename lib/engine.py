#!/usr/bin/env python3
import functools
from pathlib import Path
from constants import INDEX, HOME
import itertools


def list():
    with open(INDEX) as fd:
        for line in fd.readlines():
            yield Path(line.strip()).parent
            #yield MarkedDir(line.strip())

def _glob(path):
    try: return path.glob('*')
    except PermissionError: return []
def _isdir(path):
    try: return path.is_dir()
    except PermissionError: return False

def lines4block(block):
    lines = block.split('\n')
    lines = [ xx.strip() for xx in lines ]
    lines = [ xx for xx in lines if xx ]
    return lines


WALK_EXCLUDE= lines4block("""

    Volumes/Macintosh HD

"""
)
print(WALK_EXCLUDE)

def _walk( ot, depth=0 ):
    self=_walk
    if str(root) in WALK_EXCLUDE:
        return
    if depth < 0:
        return
    yield(path)
    for i
    if _isdir(path):
        for path in _glob(root):

    for path in _glob(root):
            continue
        yield path
        if _isdir(path):
            for path in self(path, depth-1):
                yield path

def candidates ():
    return itertools.chain(
        _walk(Path('/Volumes'), 3)
        , _walk(Path('/media'  ), 3)
        , _walk(Path('/mount'  ), 3)
        , _walk(Path('/mnt'    ), 3)
        , _walk(HOME , 5)
    )
MARKDIR_NAME='.named'
MARKFILE_NAME='name.txt'



def _md  (p): return p/MARKDIR_NAME
def _mf  (p): return p/MARKDIR_NAME/MARKFILE_NAME
def _ms  (p): return ( _mf(p).is_file() and _mf(p).read_text().strip() ) or  "nomark"

def build ():
    with open(INDEX, 'w') as fd:
        for path in candidates():
            try:
                md = _md(path)
                if md.is_dir():
                    print(path)
                    fd.write(str(md) + '\n')
            except PermissionError:
                pass


class MarkedDir :
    def __init__( self, path ):
        self._markd = Path(path)
        self._root = self._markd.parent
    def __repr__( self ):
        return '%s : %s' % (self.mark(), self.root())
    def root(self):
        return self._root
    def markd(self):
        return self._markd
    def mark(self):
        markfile = self.markd()/'name.txt'
        if markfile.exists():
            return markfile.read_text().strip()
        else:
            return "nomark"

