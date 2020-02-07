#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import argparse
import git

from geoip import geolite2
from datetime import datetime

class col:
    GRE  = '\033[92m'
    RED  = '\033[91m'
    YEL  = '\033[93m'
    END  = '\033[0m'

header = '''
      ┌─┐┌┬┐┌┐ ┬ ┬┌─┐┬ ┬
      ├─┤│││├┴┐│ │└─┐├─┤
      ┴ ┴┴ ┴└─┘└─┘└─┘┴ ┴ IP locator'''

def usage():
    parser = argparse.ArgumentParser(prog = 'Ambush')
    parser.add_argument('target', help='set an IP address')
    parser.add_argument('-q', '--quiet', help='suppress header', action='store_true')
    parser.add_argument('-u', '--update', help='', action='store_true')
    # print header with help message and exit
    if len(sys.argv) < 2:
        print(header)
        parser.print_help()
        sys.exit(0)
    return parser.parse_args()

def _print_ambush(quiet):
    if not quiet:
        print
        print '-' * 50
        print (col.GRE+'Date and Time:'+col.END), datetime.now()
        print(header)
        print col.RED+'By:'+col.END, col.YEL+'InsaneGroove'+col.END
        print col.RED+'github.com/'+col.END, col.YEL+'InsaneGroove'+col.END
        print '-' * 50
        print

def work():
    args = usage()
    _print_ambush(args.quiet)
    # update ambush
    if args.update:
        git = git.cmd.Git(git_dir)
        git.pull

    target = args.target

    if not target:
        print '[!] Wrong target'
        work()

    match = geolite2.lookup(target)

    if match is not None:
        utils.match(match)

        sys.exit()

work()
