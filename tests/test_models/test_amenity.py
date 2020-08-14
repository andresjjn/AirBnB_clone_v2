#!/usr/bin/python3
""" Unittest for ``/models/amenity.py``
class Amenity:
    class attributes:
        - __tablename__
        - name
    0. __init__(self, *args, **kwargs) inherited from 'BaseModel'
python3 -m unittest tests/test_models/test_amenity.py
"""
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    ------------------------------------------------------------
    class attributes
    ------------------------------------------------------------
    """

    """
    ------------------------------------------------------------
    0. __init__(self, *args, **kwargs) inherited from 'BaseModel'
    ------------------------------------------------------------
    """
    def test_init_without_kwargs(self):
        """ test default init (attrs since BaseModel) """
        a = Amenity()
        self.assertTrue('id' in a.__dict__)
        self.assertTrue('created_at' in a.__dict__)
        self.assertTrue('updated_at' in a.__dict__)
        self.assertIsInstance(a, BaseModel)

    def test_init_with_kwargs(self):
        """ test constructor: with **kwargs (attrs since BaseModel + attrs) """
        a = Amenity(**{'id': "aaaaaaaaa"})
        """ must not create the key: __class__ """
        self.assertFalse('__class__' in a.__dict__)
        """ must create the keys """
        self.assertTrue('id' in a.__dict__)
        self.assertTrue('created_at' in a.__dict__)
        self.assertTrue('updated_at' in a.__dict__)
