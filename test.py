#!/usr/bin/python

from dbc import DBCFile
from dbc.dtypes import UInt32, String, Int32

class ChatProfanityDBC(DBCFile):
    skeleton = [
        UInt32('id'),
        String('word'),
        Int32('lang'), #TODO: Implement Enum?
    ]

words = ChatProfanityDBC('ChatProfanity.dbc').read()
for word in words:
    if word['lang'] in (-1, 0):
        print word['word']
