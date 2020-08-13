#!/usr/bin/python3
""" Unittest for ``/models/city.py``
class City:
    class attributes:
        - __tablename__
        - name
        - state_id
        - places
    0. __init__(self, *args, **kwargs) inherited from 'BaseModel'
python3 -m unittest tests/test_models/test_city.py
"""
import unittest
from models.base_model import BaseModel
from models.city import City


class test_City(unittest.TestCase):
    """
    ------------------------------------------------------------
    class attributes
    ------------------------------------------------------------
    """
    def test_class_attributes(self):
        """ tests for class attributes """
        self.assertTrue('__tablename__' in City.__dict__)
        self.assertTrue('name' in City.__dict__)
        self.assertTrue('state_id' in City.__dict__)
        self.assertTrue('places' in City.__dict__)

    def test_type_attributes(self):
        """ check type """
        self.assertIsInstance(City.__tablename__, str)

    """
    ------------------------------------------------------------
    0. __init__(self, *args, **kwargs) inherited from 'BaseModel'
    ------------------------------------------------------------
    """
    def test_init_without_kwargs(self):
        """ test default init (attrs since BaseModel) """
        c = City()
        self.assertTrue('id' in c.__dict__)
        self.assertTrue('created_at' in c.__dict__)
        self.assertTrue('updated_at' in c.__dict__)
        self.assertIsInstance(c, BaseModel)

    def test_init_with_kwargs(self):
        """ test constructor: with **kwargs (attrs since BaseModel + attrs) """
        c = City(**{'__class__': "SomeClass",
                    'id': "aaaaaa",
                    'created_at': "2020-06-29T15:27:48.421135",
                    'updated_at': "2020-06-29T15:27:48.421148",
                    'name': "Medellin"})
        """ must not create the key: __class__ """
        self.assertFalse('__class__' in c.__dict__)
        """ must create the keys """
        self.assertTrue('id' in c.__dict__)
        self.assertTrue('created_at' in c.__dict__)
        self.assertTrue('updated_at' in c.__dict__)
        self.assertTrue('name' in c.__dict__)
