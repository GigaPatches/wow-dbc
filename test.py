#!/usr/bin/env python

from dbc import *

data = GameTipsDBC('GameTips.dbc').read()

print data[0]