#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of thalamus.
# https://github.com/Visceras/Thalamus

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2015, Francisco J. Piedrahita <franciscojpiedrahita@gmail.com>


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
