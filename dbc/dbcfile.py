#!/usr/bin/env python

import os
from struct import Struct

from dtypes import *

class DBCFile(object):
    """
    Base representation of a DBC file.
    """
    
    header_struct = Struct('4s4i')

    def __init__(self, filename, skele=None, verbose=False):
        self.filename = filename
        self.verbose = verbose
        if not hasattr(self, 'skeleton'):
            self.skeleton = skele
        self.__create_struct()
   
    def __iter__(self):
        "Iterated based approach to the dbc reading"
        if not os.path.exists(self.filename):
            raise Exception("File '%s' not found" % (self.filename,))
        
        f = file(self.filename, 'rb')

        # Read in header
        sig, records, fields, record_size, string_block_size = \
                self.header_struct.unpack(f.read(20))

        # Check signature
        if sig != 'WDBC':
            f.close()
            raise Exception('Invalid file type')

        self.records = records
        self.fields = fields
        self.record_size = record_size
        self.string_block_size = string_block_size
       
        if not self.struct:
            # If the struct doesn't exist, create a default one
            self.skeleton = Array('data', Int32, fields)
            self.__create_struct()

        # Ensure that struct and record_size is the same
        if self.struct.size != record_size:
            f.close()
            raise Exception('Struct size mismatch (%d != %d)' % \
                            (self.struct.size, record_size))
        
        # Read in string block
        f.seek(20 + records * record_size)
        self.string_block = f.read(string_block_size)
        f.seek(20)

        try:
            for i in xrange(records):
                data = self.struct.unpack(f.read(record_size))
                yield self.__process_record(data)
        finally:
            f.close()

    def __create_struct(self):
        "Creates a Struct from the Skeleton"
        if self.skeleton:
            s = ['<']
            for item in self.skeleton:
                if isinstance(item, Array):
                    s.extend(x.c for x in item.items)
                else:
                    s.append(item.c)
            self.struct = Struct(''.join(s))
        else:
            self.struct = None

    def __process_record(self, data):
        "Processes a record (row of data)"
        output = {}
        i = 0
        d = 0
        while i < len(self.skeleton):
            if isinstance(self.skeleton[i], Array):
                temp = []
                for t in self.skeleton[i].items:
                    t = self.__process_field(t, data[d])
                    if t:
                        temp.append(t[0])
                        d += 1
                if temp:
                    output[self.skeleton[i].name] = temp
            else:
                t = self.__process_field(self.skeleton[i], data[d])
                if t:
                    output.update(t)
                    d += 1
            i += 1
        return output
    
    def __process_field(self, _type, data):
        "Processes a field inside a record"
        output = {}
        name = _type.name if _type.name else 0 # Default to name of 0 (for arrays)
        if isinstance(_type, String):
            if data == 0:
                output[name] = unicode('', 'utf-8')
            else:
                if data > self.string_block_size or self.string_block[data - 1] != '\0':
                    raise Exception('Invalid string')
                s = self.string_block[data:self.string_block.index('\0', data)]
                output[name] = unicode(s, 'utf-8')
        elif not isinstance(_type, PadByte): # Ignore PadBytes
            output[name] = data
        return output

