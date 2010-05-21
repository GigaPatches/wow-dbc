#!/usr/bin/env python

"""
"""

class Base(object):
    "Base type, just includes a name"
    def __init__(self, name=''):
        self.name = name

class Int32(Base):
    c = 'i'

class UInt32(Base):
    c = 'I'

class Int64(Base):
    c = 'q'

class UInt64(Base):
    c = 'Q'

class Float(Base):
    c = 'f'

class String(Base):
    c = 'I'

class PadByte(Base):
    def __init__(self, size=4):
        super(PadByte, self).__init__()
        if size < 0:
            size = 1
        self.c = '%dx' % (size,)

class Array(Base):
    def __init__(self, name, _type, count):
        super(Array, self).__init__(name)
        self.items = [_type()] * count

class Localization(Array):
    def __init__(self, name):
        super(Localization, self).__init__(name, String, 16)
        self.items.append(UInt32())
