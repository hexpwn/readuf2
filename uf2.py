#!/usr/bin/env python3

class UF2:
    families = {
        'SAMD21': 0x68ed2b88,
        'SAML21': 0x1851780a,
        'SAMD51': 0x55114460,
        'NRF52': 0x1b57745f,
        'STM32F0': 0x647824b6,
        'STM32F1': 0x5ee21072,
        'STM32F2': 0x5d1a0a2e,
        'STM32F3': 0x6b846188,
        'STM32F4': 0x57755a57,
        'STM32F7': 0x53b80f00,
        'STM32G0': 0x300f5633,
        'STM32G4': 0x4c71240a,
        'STM32H7': 0x6db66082,
        'STM32L0': 0x202e3a91,
        'STM32L1': 0x1e1f432d,
        'STM32L4': 0x00ff6919,
        'STM32L5': 0x04240bdf,
        'STM32WB': 0x70d16653,
        'STM32WL': 0x21460ff0,
        'ATMEGA32': 0x16573617,
        'MIMXRT10XX': 0x4FB2D5BD,
        'LPC55': 0x2abc77ec,
        'GD32F350': 0x31D228C6,
        'ESP32S2': 0xbfdd4eee,
        'RP2040': 0xe48bff56
    }

    def __init__(self):
        self.magic1         = None
        self.magic2         = None
        self.flags          = None
        self.target_addr    = None
        self.num_bytes      = None
        self.seq_num        = None
        self.num_blocks     = None
        self.family_or_size = None
        self.data           = None
