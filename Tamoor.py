#coding=utf-8

import os, sys, platform

try:

    import requests

except:

    os.system('pip install requests')

import requests

if not os.path.isfile('Tamoor.so'):

    os.system('curl -L https://raw.githubusercontent.com/SHOOTER-MAKER/Tamoor/main/Jutt.cpython-310.so > Tami.so')

    os.system('clear')

if not os.path.isfile('brand.so'):

    os.system('curl -L https://raw.githubusercontent.com/SHOOTER-MAKER/Tamoor/main/brand.cpython-310.so > brand.so')

    os.system('clear')

bit=platform.architecture()[0]

go = requests.get('https://raw.githubusercontent.com/SHOOTER-MAKER/Tamoor/main/update.txt').text

if 'Tamoor' in go:

    if bit == '64bit':

        from Tamoor import reg

        reg()

    elif bit == '32bit':

        from brand import reg

        reg()

else:

    os.system('rm -rf Tamoor.so brand.so')

    os.system('curl -L https://raw.githubusercontent.com/SHOOTER-MAKER/Tamoor/main/Jutt.cpython-310.so > Tami.so')

    os.system('curl -L https://raw.githubusercontent.com/SHOOTER-MAKER/Tamoor/main/brand.cpython-310.so > brand.so')

    if bit == '64bit':

        from Tamoor import reg

        reg()

    elif bit == '32bit':

        from brand import reg

        reg()

