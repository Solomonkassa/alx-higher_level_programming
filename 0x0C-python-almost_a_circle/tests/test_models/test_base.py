#!/usr/bin/python3
"""Unittest for Base class"""
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Runs tests for base.py"""

    @classmethod
    def setUpClass(cls):
        """Sets up the testing environment"""

        Base._Base__nb_objects = 0
        cls.b1 = Base()
        cls.b2 = Base()
        cls.b3 = Base(22)
        cls.b4 = Base(2.2)
        cls.b5 = Base("two")
        cls.r1 = Rectangle(10, 7, 2, 8)
        cls.r2 = Rectangle(2, 4)

    def test_0_0_create(self):
        """Tests the creation of a Base class"""

        self.assertTrue(self.b1)

    def test_0_1_create_id(self):
        """Tests the creation of class Base with a specified id"""

        self.b1.id = 5
        self.assertEqual(self.b1.id, 5)

    def test_0_2_id_inc(self):
        """Test to see if id is incrementing correctly"""

        self.b1.id = 1
        test = self.b1.id
        test2 = self.b2.id
        self.assertEqual(test, test2 - 1)

    def test_0_3_id_inc2(self):
        """More id incrementation tests"""

        test = self.b1.id
        test2 = self.b2.id
        test3 = self.b3.id
        self.assertEqual(test, test2 - 1)
        self.assertEqual(test3, 22)

    def test_0_4_id_test(self):
        """Checks ids"""

        self.assertTrue(self.b1, 1)
        self.assertTrue(self.b2, 2)
        self.assertTrue(self.b3, 22)
        self.assertTrue(self.b4, 2.2)
        self.assertTrue(self.b5, "two")

    def test_15_0_toJsonString(self):
        """Tests if the JSON string representation is working"""

        dictionary = self.r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertTrue(type(dictionary), dict)
        self.assertTrue(type(json_dictionary), str)

    def test_16_0_saveToFile(self):
        """Checks to make sure a file is created and written to"""

        Rectangle.save_to_file([self.r1, self.r2])
        self.assertTrue(os.path.isfile("Rectangle.json"))

    def test_17_0_fromJsonString(self):
        """Checks a list of JSON string format"""

        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertTrue(type(list_input), list)
        self.assertTrue(type(json_list_input), str)
        self.assertTrue(type(list_output), list)

    def test_18_0_create(self):
        """Tests the create method"""

        r1_dict = self.r1.to_dictionary()
        r = Rectangle.create(**r1_dict)
        self.assertFalse(self.r1 == r)
        self.assertFalse(self.r1 is r)

    @classmethod
    def tearDownClass(cls):
        """Breaks down the testing environment"""

        pass
