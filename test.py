#!/usr/bin/env python

from dbc import *

spells = SpellDBC('Spell.dbc')

for spell in spells:
    print spell['SpellName'][0]
