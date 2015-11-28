import types

class Packet(object):
    """
    MQTT Packet structure
    """

    def __init__(self, header=None, payload=None):
        self.header = header
        self.payload = payload


class Header(object):
    """
    Handles the Fixed Header and the Variable header
    in order to simplify the passing of arguments to the
    Packet class
    """

    def __init__(self, fixed=None, variable=None):
        self.fixed = fixed
        self.variable = variable


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

    def __init__(self, packet_type=None, dup=None, qos=None, retain=None):
        self.packet_type = packet_type

        self.dup = dup
        self.qos = qos
        self.retain = retain


class Variable(object):
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

    def __init__(self, msb=None, lsb=None):
        self.msb = msb
        self.lsb = lsb
