#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of thalamus.
# https://github.com/Visceras/Thalamus

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2015, Francisco J. Piedrahita <franciscojpiedrahita@gmail.com>

from preggy import expect

from tests.base import TestCase

import thalamus.mqtt_protocol as Protocol


class PacketTestCase(TestCase):

    def test_header(self):
        self.packet = Protocol.Packet()
        expect(self.packet.header).to_equal(None)

    def test_packet(self):
        self.packet = Protocol.Packet()
        expect(self.packet.payload).to_equal(None)


class HeaderTestCase(TestCase):

    def test_fixed(self):
        header = Protocol.Header()
        expect(header.fixed).to_equal(None)

    def test_variable(self):
        header = Protocol.Header()
        expect(header.variable).to_equal(None)


class FixedTestCase(TestCase):

    def test_packet_type(self):
        fixed = Protocol.Fixed()
        expect(fixed.packet_type).to_equal(None)

    def test_flags(self):
        fixed = Protocol.Fixed()
        expect(fixed.packet_flags).to_equal(None)

    def test_length(self):
        fixed = Protocol.Fixed()
        expect(fixed.packet_length).to_equal(None)


class ConnectTestCase(TestCase):

    def test_client_id(self):
        connect = Protocol.Connect()
        expect(connect.client_id).to_equal(None)

    def test_keep_alive(self):
        connect = Protocol.Connect()
        expect(connect.keep_alive).to_equal(None)

    def test_proto_ver(self):
        connect = Protocol.Connect()
        expect(connect.proto_ver).to_equal(0x04)

    def test_proto_name(self):
        connect = Protocol.Connect()
        expect(connect.proto_name).to_equal("MQTT")
