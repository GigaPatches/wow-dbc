#!/usr/bin/env python

"""
"""

class Base(object):
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

class Array(Base):
    def __init__(self, name, _type, count):
        super(Array, self).__init__(name)
        self.items = [_type()] * count

class Localization(Array):
    def __init__(self, name):
        super(Localization, self).__init__(name, String, 16)
        self.items.append(UInt32())