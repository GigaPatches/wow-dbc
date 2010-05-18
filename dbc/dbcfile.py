#!/usr/bin/env python

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
        if not hasattr(self, 'skeleton'):
            self.skeleton = skele
        self.__create_struct()  
    
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

        print '%s Info:' % (self.filename,)
        print 'Records: %s, Fields: %s, Record Size: %s, String Block: %s' % \
                (records, fields, record_size, string_block_size)

        if not self.struct:
            # Default to reading in all ints
            self.skeleton = [Int32(str(x)) for x in range(0, fields)]
            self.__create_struct()

        if self.struct.size != record_size:
            f.close()
            raise Exception('Struct size mismatch')

        self.string_offset = 20 + records * record_size
        self.string_end = self.string_offset + string_block_size
        
        output = []
        for i in  xrange(records):
            data = self.struct.unpack(f.read(record_size))
            output.append(self.__process(data))
            f.seek(20 + i * record_size)
        f.close()

        return output

    def __create_struct(self):
        "Creates a Struct from the Skeleton"
        if self.skeleton:
            s = []
            for item in self.skeleton:
                if isinstance(item, Array):
                    s.extend(x.c for x in item.items)
                else:
                    s.append(item.c)
            self.struct = Struct(''.join(s))
        else:
            self.struct = None

    def __process(self, data):
        output = {}
        for i in xrange(len(self.skeleton)):
            t = self.skeleton[i]
            if isinstance(t, String):
                if data[i] == 0 or data[i] >= self.string_end:
                    output[t.name] = unicode('', 'utf-8')
                else:
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
   
   