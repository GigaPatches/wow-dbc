#!/usr/bin/python
"""
"""

import os
from struct import Struct
from dtypes import *

class DBCFile(object):
    """
    Base representation of a DBC file.
    """
    
    header_struct = Struct('4s4i')

    def __init__(self, filename, skele=None):
        self.filename = filename
        if skele:
            self.skeleton = skele
        if self.skeleton:
            self.struct = Struct(''.join(x.c for x in self.skeleton))
    
    def read(self):
        if not os.path.exists(self.filename):
            raise Exception('File Not Found')
        f = file(self.filename, 'rb')
        self.__file = f

        sig, records, fields, record_size, string_block_size = \
            self.header_struct.unpack(f.read(20))

        if sig != 'WDBC':
            f.close()
            raise Exception('Invalid file type')

        if not self.struct:
            # Default to reading in all ints
            #TODO: Guess format types
            self.struct = Struct('i' * fields)

        if self.struct.size != record_size:
            f.close()
            raise Exception('Struct size mismatch')

        self.string_offset = 20 + records * record_size
        output = []
        for i in  xrange(records):
            data = self.struct.unpack(f.read(record_size))
            output.append(self.__process(data))
            f.seek(20 + i * record_size)
        f.close()

        return output

    def __process(self, data):
        output = {}
        for i in xrange(len(self.skeleton)):
            t = self.skeleton[i]
            if isinstance(t, String):
                # String processing
                self.__file.seek(self.string_offset + data[i])
                s = ''
                while '\0' not in s:
                    s += self.__file.read(128)
                s = s[:s.index('\0')]
                output[t.name] = unicode(s, 'utf-8')
            else:
                output[t.name] = data[i]
        return output
