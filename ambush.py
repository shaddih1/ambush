# coding: utf-8

from geoip import geolite2

print('''
      ┌─┐┌┬┐┌┐ ┬ ┬┌─┐┬ ┬
      ├─┤│││├┴┐│ │└─┐├─┤
      ┴ ┴┴ ┴└─┘└─┘└─┘┴ ┴ IP locator\033[31m
      By:\033[0m \033[33mPudwill\033[0m \033[31m
      github.com/\033[33mPudwill\033[0m
      ''')

print('**Please use \033[32m\'\'\033[0m before typing the IP as the example shows.**')
print('Example:\033[32m \'\033[0m192.168.0.1\033[32m\'\033[0m\n')
_ip_ = input('\033[32mWhat\'s the IP?: \033[0m')
while _ip_ is int:
    print('try again')

match = geolite2.lookup(_ip_)

if match is not None:
    print('\033[32mcountry:\033[0m') , match.country
    print('\033[32mContinent:\033[0m') , match.continent
    print('\033[32mTime zone:\033[0m') , match.timezone
    print('\033[32mSubdivisions:\033[0m') , match.subdivisions
    print('\033[44mThanks for use Ambush.\033[0m\n')


