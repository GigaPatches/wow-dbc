#!/usr/bin/env python

from dbcfile import DBCFile
from dtypes import UInt32, String, Int32

class ChatProfanityDBC(DBCFile):
    skeleton = [
        UInt32('id'),
        String('word'),
        Int32('lang'), #TODO: Implement Enum?
    ]