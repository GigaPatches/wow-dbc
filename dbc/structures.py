#!/usr/bin/env python

from dbcfile import DBCFile
from dtypes import UInt32, String, Int32

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
        String('Locale0'),
        String('Locale1'),
        String('Locale2'),
        String('Locale3'),
        String('Locale4'),
        String('Locale5'),
        String('Locale6'),
        String('Locale7'),
        String('Locale8'),
        String('Locale9'),
        String('Locale10'),
        String('Locale11'),
        String('Locale12'),
        String('Locale13'),
        String('Locale14'),
        UInt32('LocaleMask'),
    ]
