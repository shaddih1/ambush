# -*- coding: utf-8 -*-

import git
from datetime import datetime

def update():
    git = git.cmd.Git(git_dir)
    git.pull

def total():
    time1 = datetime.now()
    time2 = datetime.now()
    total = time2 - time1

    return total

def match(match):
    print(col.GRE+'country: '+col.END) , match.country
    print(col.GRE+'Continent: '+col.END) , match.continent
    print(col.GRE+'Time zone: '+col.END) , match.timezone
    print(col.GRE+'Subdivisions: '+col.END) , match.subdivisions
    print (col.GRE+'Finished location in: '+col.END), total()
    print
    print(col.RED+'Thanks for using Ambush.'+col.END)
    print
