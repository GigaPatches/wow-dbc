#!/usr/bin/env python

from dbc import *

words = ChatProfanityDBC('ChatProfanity.dbc').read()
for word in words:
    if word['lang'] in (-1, 0):
        print word['word']
