#!/usr/bin/env python

from dbcfile import DBCFile
from dtypes import UInt32, String, Int32, Array

class ChatProfanityDBC(DBCFile):
    skeleton = [
        UInt32('id'),
        String('word'),
        Int32('lang'),
    ]
    
class GameTipsDBC(DBCFile):
    skeleton = [
        UInt32('ID'),
        String('RefName'),
        Array('Locale', String, 15),
        UInt32('LocaleMask'),
    ]
