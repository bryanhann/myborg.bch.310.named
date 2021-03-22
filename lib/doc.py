#!/usr/bin/env python3

from constants import *
import templates
from myparser import ARGS
from myparser import die as DIE


_fixline = lambda line : PADDING + line.strip()
_dlines  = lambda fn : str(fn.__doc__).split(NEWLINE)
longhelp  = lambda fn : NEWLINE.join( map( _fixline, _dlines(fn) ) )
shorthelp = lambda fn : str(fn.__doc__).split('\n')[0]

def user_help(cmdDict):
    if ARGS.ARGS:
        return __help_subcommand(cmdDict)
    else:
        return __help_main(cmdDict)


def __help_main(cmdDict):
    print( (templates.USAGE % PROG).strip() )
    items = cmdDict.items()
    names = [ x[0] for x in items ]
    funcs = [ x[1] for x in items ]
    n = max(map(len,names))
    for name,func in zip(names,funcs):
        sep = ' -- '
        print(PADDING + name.ljust(n) + sep + shorthelp(func) )

def __help_subcommand(cmdDict):
    name = ARGS.ARGS[0]
    fn = cmdDict.get(name,None)
    if fn is None:
        DIE( 1,  "'%s' is not a subcommand" % name )
    else:
        print ('DOCSTRING:')
        print(longhelp(fn))

