#!/usr/bin/env python
# -*- coding: utf-8 -*-
from unittest import TestCase
from mosaicomponents.checkfield import CheckField
# Se for usar o py.test:
# Comentar a linha acima, e descomentar a de baixo
#from mosaicomponents.mosaicomponents.checkfield import CheckField

class TestCheckField(TestCase):

    def setUp(self):
        """Do the test basic setup."""
        data = {"label": ("Type"), "name":"type", "value": True}
        self.checkfield = CheckField(data, self)

    # ----------------------------------------------------------------------
    def test_get_value(self):
        self.assertTrue(self.checkfield.get_value())

    # ----------------------------------------------------------------------
    def test_set_value(self):
        value = "Teste"
        self.assertIsNone(self.checkfield.set_value(value))
        value = "True"
        self.assertIsNone(self.checkfield.set_value(value))
        value = True
        self.assertIsNone(self.checkfield.set_value(value))
        value = "Algo"
        self.assertIsNone(self.checkfield.set_value(value))
