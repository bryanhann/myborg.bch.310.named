#!/usr/bin/env python3

import engine as II
import handle as HH
from parser import die as DIE

def user_list():
    args = HH.args()
    for named in II.list():
        print(named)

def user_build():
    """Rebuild an index.

    This can take a whild
    """
    II.build()

def user_find():
    args = HH.args('name')
    for hit in II.find(args.name):
        print(hit)

def user_unique():
    args = HH.args('name')
    hits = II.find(args.name)
    if len(hits) < 1: DIE(1, 'no hits')
    if len(hits) > 1: DIE(1, 'multiple hits')
    print(hits[0])

def user_help():
    HH.user_help()

