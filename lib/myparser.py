import argparse
try:
    ARGS
except NameError:
    parser=argparse.ArgumentParser()
    parser.add_argument('CMD', action="store", default='help', nargs='?')
    parser.add_argument('ARGS' , action="store", nargs='*', default=[])
    parser.add_argument('--sub' , action="store", nargs='*', default=[])
    ARGS = parser.parse_args()
    _ARGS = ARGS.ARGS
    _CMD = ARGS.CMD
def die(err, msg):
    import sys
    PROG=sys.argv[0].split('/')[-1]
    sys.stderr.write('ERROR(%s:%s) -- %s\n' % (PROG, ARGS.CMD, msg))
    exit(err)

