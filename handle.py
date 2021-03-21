import sys

#from parser import ARGS
from parser import _ARGS, _CMD
from parser import die as DIE
from constants import *
import doc
import user

def args(*names):
    class Namespace: pass
    if not len(_ARGS)==len(names):
        DIE(97, 'Expectes %s args but received %s.' % (len(names), len(_ARGS)))
    acc = Namespace()
    for key,val in zip(names,_ARGS):
        setattr(acc,key,val)
    return acc


def cmdDict_4_mod(mod):
    prefix = 'user_'
    acc={}
    for name in dir(mod):
        if name.startswith(prefix):
            key = name[len(prefix):]
            val = getattr(mod,name)
            acc[key] = val
    return acc

def user_help():
    doc.user_help(cmdDict_4_mod(user))



def main():
    cmdDict = cmdDict_4_mod(user)
    fn = cmdDict.get( _CMD, None )
    if fn is None:
        DIE(99, "unrecognized command. Try '%s help'." % PROG )
    else:
        exit( fn() )

