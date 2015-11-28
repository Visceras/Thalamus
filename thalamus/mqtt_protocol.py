#import types
#import binascii

class Flag(object):

    length = 1

    def __init__(self, value):
        self.value = value

    @classmethod
    def convert(cls, args):
        value = 0
        values = [flag.value for flag in reversed(args)]

        for index, val in enumerate(values):
            value = (val << index) | value

        return value

    @classmethod
    def length_error(cls, method, length, values):
        if len(values) != length:
            err = "{}() takes exactly {} arguments ({} given)"
            raise ValueError(err.format(method, length, len(values)))

    @classmethod
    def flags_to_nibble(cls, *args):
        method_name = "flags_to_nibble"
        cls.length_error(method_name, 4, args)

        value = cls.convert(args)
        return Nibble(value)

    @classmethod
    def flags_to_byte(cls, *args):
        method_name = "flags_to_byte"
        cls.length_error(method_name, 8, args)

        value = cls.convert(args)
        return Byte(value)


class Nibble(object):

    length = 4

    def __init__(self, value):
        self.value = value

    @staticmethod
    def add_nibbles(nibble_1, nibble_2):
        value = (nibble_1.value << 4) | nibble_2.value
        return Byte(value)

class Byte(object):

    length = 8

    def __init__(self, value):
        self.value = value


class Packet(object):
    """
    MQTT Packet structure
    """

    def __init__(self):
        self.header = None
        self.payload = None

class Header(object):
    """
    Handles the Fixed Header and the Variable header
    in order to simplify the passing of arguments to the
    Packet class
    """

    def __init__(self):
        self.fixed = None
        self.variable = None


class Fixed(object):
    """
    Each MQTT Control Packet contain a fixed header.

            +----------------------------------------+
            |               FIXED HEADER             |
            +--------+---+---+---+---+---+---+---+---+
            |   Bit  | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
            +--------+---+---+---+---+---+---+---+---+
            | Byte 1 | Packet Type   | Packet Flags  |
            +--------+---------------+---------------+
            | Byte 2 |       Remaining Length        |
            +--------+-------------------------------+
    """

    def __init__(self):
        self.packet_type = None

        self.dup = None
        self.qos = None
        self.retain = None


class Connect(object):
    """
    The variable header component of many of the control packet types
    includes a two byte Packet Identifier field.

            +----------------------------------------+
            |             VARIABLE HEADER            |
            +--------+---+---+---+---+---+---+---+---+
            |   Bit  | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
            +--------+---+---+---+---+---+---+---+---+
            | Byte 1 |     Packet Identifier MSB     |
            +--------+-------------------------------+
            | Byte 2 |     Packet Identifier LSB     |
            +--------+-------------------------------+
    """

    def __init__(self):
        pass
