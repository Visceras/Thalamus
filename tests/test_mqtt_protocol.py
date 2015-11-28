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

    def test_dup(self):
        fixed = Protocol.Fixed()
        expect(fixed.dup).to_equal(None)

    def test_qos(self):
        fixed = Protocol.Fixed()
        expect(fixed.qos).to_equal(None)

    def test_request(self):
        fixed = Protocol.Fixed()
        expect(fixed.retain).to_equal(None)
