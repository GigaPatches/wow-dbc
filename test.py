#!/usr/bin/env python

from dbc import *

spells = SpellDBC('Spell.dbc')

for spell in spells:
    #print ', '.join(x for x in dir(spell) if not x.startswith('__'))
    print spell.SpellName[0]
    break
