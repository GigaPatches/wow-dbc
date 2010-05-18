#!/usr/bin/env python

from dbc import *

data = GameTipsDBC('GameTips.dbc').read()
for tip in data:
    print tip['RefName']