#!/usr/bin/env python3

import sys
import os
from pathlib import Path

PROG=Path(sys.argv[0]).name
HOME=Path(os.environ['HOME'])
INDEX=HOME/'.cache/named/index'
NEWLINE='\n'
PADDING=' '*8

