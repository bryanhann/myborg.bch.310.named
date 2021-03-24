import sys
from constants import *
import argparse
try:
    ARGS
except NameError:
    parser=argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()

    group.add_argument("-v", "--verbose", action="store_true")
    group.add_argument("-q", "--quiet", action="store_true")
    group.add_argument('-f', '--find', metavar='NAME',type=str, help="list dirs named NAME" )
    group.add_argument('-l', '--list', action="store_true", help="list all named dirs.")

    parser.add_argument('-u', '--unique', action="store_true", help="with -f, require a unique result.")
    parser.add_argument('-b', '--build', action="store_true", help="rebuild the index before all" )
    ARGS = parser.parse_args()

def main():
    if ARGS.build:
        user_build()
        #cmdDict['build']()
    if ARGS.list: 
        user_list()
        #cmdDict['list']() 
    elif ARGS.find:
        user_find(ARGS.find)
        #cmdDict['find'](ARGS.find)


import engine

def user_list():
    for named in engine.list():
        print(named)

def user_build():
    """Rebuild an index.

    This can take a whild
    """
    engine.build()

def user_find(name):
    hits=engine.find(name)
    for hit in hits:
        print(hit.root())



