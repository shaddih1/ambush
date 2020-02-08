#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, argparse, subprocess
from datetime import datetime
from geoip import geolite2
GREEN, RED, YELLOW, END = '\033[92m', '\033[91m', '\033[93m', '\033[0m'

header = '''
┌─┐┌┬┐┌┐ ┬ ┬┌─┐┬ ┬
├─┤│││├┴┐│ │└─┐├─┤
┴ ┴┴ ┴└─┘└─┘└─┘┴ ┴ IP locator'''

def shutdown():
    print(RED+'\nThanks for using Ambush.\n'+END)
    sys.exit(0)

# display heading
def _print_header(quiet):
    if not quiet:
        lines = '-' * 50
        print ('\n' + lines)
        print (GREEN+'Date and Time:'+END), datetime.now()
        print(header)
        print RED+'By:'+END, YELLOW+'InsaneGroove'+END
        print RED+'github.com/'+END, YELLOW+'InsaneGroove'+END
        print (lines)

def usage():
    parser = argparse.ArgumentParser()
    parser.add_argument('target', help='set a target to locate')
    parser.add_argument('-u', '--update', help='update Ambush to the lastest version', action='store_true')
    parser.add_argument('-q', '--quiet', help='suppress header', action='store_true')
    if len(sys.argv) < 2:
        print(header + '\n')
        parser.print_help()
        sys.exit(0)
    return parser.parse_args()

def work(target):
    time1 = datetime.now()
    time2 = datetime.now()
    total = time2 - time1

    try:
        match = geolite2.lookup(target)

        if match is not None:
            print(GREEN+'\ncountry: '+END) , match.country
            print(GREEN+'Continent: '+END) , match.continent
            print(GREEN+'Time zone: '+END) , match.timezone
            print(GREEN+'Subdivisions: '+END) , match.subdivisions
            print (GREEN+'Finished location in: '+END), total
            shutdown()
    except ValueError:
        print('\n[!] Wrong target, please try again\n')

def main():
    args = usage()
    # update Ambush
    if args.update:
        update = subprocess.call(["git", "pull"])
    _print_header(args.quiet)
    work(args.target)

main()
