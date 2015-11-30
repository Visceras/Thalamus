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
        self.packet_flags = None
        self.packet_length = None


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
            | Byte 3 |           'M'                 |
            +--------+-------------------------------+
            | Byte 4 |           'Q'                 |
            +--------+-------------------------------+
            | Byte 5 |           'T'                 |
            +--------+-------------------------------+
            | Byte 6 |           'T'                 |
            +--------+---+---+---+---+---+---+---+---+
            | Byte 7 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
            +--------+---+---+---+---+---+---+---+---+
            |        |        User Name Flag         |
            |        |        Password Flag          |
            |        |        Will Retain            |
            | Byte 8 |        Will QoS               |
            |        |        Will Flag              |
            |        |        Clean Session          |
            |        |        Reserved               |
            +--------+-------------------------------+
            | Byte 9 |       Keep Alive MSB          |
            +--------+-------------------------------+
            | Byte 10|       Keep Alive LSB          |
            +--------+-------------------------------+
    """

    MQTT_PROTO_V311 = 0x04

    def __init__(self):
        # definition of Byte #1 and Byte #2
        self.packet_flags_id = None

        # Definition of Byte #3
        self.proto_ver = self.MQTT_PROTO_V311

        # Definition of Byte #3 to Byte #6
        self.proto_name = 'MQTT'

        # Definition of Byte #8 Flags
        self.username_flag = None
        self.Password_flag = None

        self.will_retain_flag = None
        self.will_qos_flag = None
        self.will_flag = None

        self.clean_session_flag = None

        # Definition of Byte #9 and Byte #10
        self.keep_alive = None

        # Payload Definition
        self.client_id = None
        self.will_topic = None
        self.will_message = None
        self.username = None
        self.password = None


class Connack(object):
    """
    The variable Header format for the CONNACK Packet:

            +----------------------------------------+
            |             VARIABLE HEADER            |
            +--------+---+---+---+---+---+---+---+---+
            |   Bit  | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
            +--------+---+---+---+---+---+---+---+---+
            | Byte 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |SP |
            +--------+---+---+---+---+---+---+---+---+
            | Byte 2 | X | X | X | X | X | X | X | X |
            +--------+---+---+---+---+---+---+---+---+

            SP: Session Present Flag.
            Byte 2: Connect Return Code.
    """

    CONNACK_ACCEPT = 0x00
    CONNACK_PROTO_VER = 0x01
    CONNACK_INVALID_ID = 0x02
    CONNACK_SERVER = 0x03
    CONNACK_CREDENTIALS = 0x04
    CONNACK_AUTH = 0x05

    def __init__(self):
        self.ack_flag = None
        self.return_code = None

class Publish(object):
    """
    A publish packet is sent from a client to a server or from a server to a
    client to transport an application Message.

            +------------------------------------------+
            |              VARIABLE HEADER             |
            +----------+---+---+---+---+---+---+---+---+
            |   Bit    | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
            +----------+---+---+---+---+---+---+---+---+
            | Byte 1   |           Length MSB          |
            +----------+-------------------------------+
            | Byte 2   |           Length LSB          |
            +----------+-------------------------------+
            | Byte 3   |                               |
            +----------+           Channel             +
            | Byte N   |                               |
            +----------+-------------------------------+
            | Byte N+1 |     Packet Identifier MSB     |
            +----------+-------------------------------+
            | Byte N+2 |     Packet Identifier LSB     |
            +----------+-------------------------------+
    """

    def __init__(self):
        self.channel = None
        self.mqtt_packet_id = None


class Puback(object):
    """
        +------------------------------------------+
        |              VARIABLE HEADER             |
        +----------+---+---+---+---+---+---+---+---+
        |   Bit    | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
        +----------+---+---+---+---+---+---+---+---+
        | Byte 1   |     Packet Identifier MSB     |
        +----------+-------------------------------+
        | Byte 2   |     Packet Identifier LSB     |
        +----------+-------------------------------+

    """

    def __init__(self):
        self.packet_id = None


class Pubrel(object):
    """
        +------------------------------------------+
        |              VARIABLE HEADER             |
        +----------+---+---+---+---+---+---+---+---+
        |   Bit    | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
        +----------+---+---+---+---+---+---+---+---+
        | Byte 1   |     Packet Identifier MSB     |
        +----------+-------------------------------+
        | Byte 2   |     Packet Identifier LSB     |
        +----------+-------------------------------+

    """

    def __init__(self):
        self.packet_id = None


class Pubcomp(object):
    """
        +------------------------------------------+
        |              VARIABLE HEADER             |
        +----------+---+---+---+---+---+---+---+---+
        |   Bit    | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
        +----------+---+---+---+---+---+---+---+---+
        | Byte 1   |     Packet Identifier MSB     |
        +----------+-------------------------------+
        | Byte 2   |     Packet Identifier LSB     |
        +----------+-------------------------------+

    """

    def __init__(self):
        self.packet_id = None


class Subscribe(object):
    """
        +------------------------------------------+
        |              VARIABLE HEADER             |
        +----------+---+---+---+---+---+---+---+---+
        |   Bit    | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
        +----------+---+---+---+---+---+---+---+---+
        | Byte 1   |         Length MSB            |
        +----------+-------------------------------+
        | Byte 2   |         Length LSB            |
        +----------+-------------------------------+
        | Byte 3   |                               |
        +----------+           Channel             +
        | Byte N   |                               |
        +----------+---+---+---+---+---+---+-------+
        | Byte N+1 | 0 | 0 | 0 | 0 | 0 | 0 |  Qos  |
        +----------+---+---+---+---+---+---+-------+
    """

    def __init__(self):
        self.mqtt_packet_id = None

        self.qos_list = None
        self.topic_filter_list = None



