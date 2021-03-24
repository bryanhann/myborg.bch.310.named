#!/usr/bin/env python3

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



