#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os

import libkarel
from kareltest import *

import unittest


class PegaditoTest(KarelTest):
    def runTest(self):
        world = self.world

        self.assertEqual(world.lista_zumbadores, {})

        self.assertEqual(world.despliega, ['UNIVERSO'])

        self.assertEqual(world.mochila, 'INFINITO')


suite = KarelTestSuite()
suite.populate(PegaditoTest)

runner = unittest.TextTestRunner()
result = runner.run(suite)
sys.exit(not result.wasSuccessful())
