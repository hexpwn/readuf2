#!/usr/bin/env python3

class UF2:
    def __init__(self, filename):
        self.filename       = filename
        self.flags          = None
        self.target_addr    = None
        self.num_bytes      = None
        self.seq_num        = None
        self.num_blocks     = None
        self.family_or_size = None
        self.data           = None
