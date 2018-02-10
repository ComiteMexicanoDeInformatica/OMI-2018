#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os

import libkarel
from kareltest import *

import unittest


class XYZTest(KarelTest):
    def runTest(self):
        world = self.world

        self.assertEqual(world.mochila, 'INFINITO')

        self.assertEqual(world.lista_zumbadores, {})

        self.assertEqual(world.despliega, ['ORIENTACION'])


suite = KarelTestSuite()
suite.populate(XYZTest)

runner = unittest.TextTestRunner()
result = runner.run(suite)
sys.exit(not result.wasSuccessful())
