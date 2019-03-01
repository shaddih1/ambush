# -*- coding: utf-8 -*-

from geoip import geolite2
 
class col:
    GRE  = '\033[92m'
    RED  = '\033[91m'
    YEL  = '\033[93m'
    BLUE = '\033[94m'
    END  = '\033[0m' 


def _print_ambush():
    print('''
      ┌─┐┌┬┐┌┐ ┬ ┬┌─┐┬ ┬
      ├─┤│││├┴┐│ │└─┐├─┤
      ┴ ┴┴ ┴└─┘└─┘└─┘┴ ┴ IP locator''')
    print col.RED+'By:'+col.END, col.YEL+'Pudwill'+col.END
    print col.RED+'github.com/'+col.END, col.YEL+'Pudwill'+col.END
    print
    
_print_ambush()

def _work():
    ip = ''
    
    _get_ = raw_input(col.GRE+'What\'s the IP?: {}'.format(ip)+col.END)
    
    match = geolite2.lookup(_get_)
    
    if match is not None:
        print(col.GRE+'country: '+col.END) , match.country
        print(col.GRE+'Continent: '+col.END) , match.continent
        print(col.GRE+'Time zone: '+col.END) , match.timezone
        print(col.GRE+'Subdivisions: '+col.END) , match.subdivisions
        print(col.GRE+'Thanks for use Ambush.'+col.END)    
    
_work()
