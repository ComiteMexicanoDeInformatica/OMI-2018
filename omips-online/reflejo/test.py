#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os

import libkarel
from kareltest import *

import unittest


class ReflejoTest(KarelTest):
    def runTest(self):
        world = self.world

        self.assertEqual(world.mochila, 'INFINITO')

        self.assertEqual(world.lista_zumbadores, {})

        self.assertEqual(world.despliega, ['UNIVERSO'])


suite = KarelTestSuite()
suite.populate(ReflejoTest)

runner = unittest.TextTestRunner()
result = runner.run(suite)
sys.exit(not result.wasSuccessful())
