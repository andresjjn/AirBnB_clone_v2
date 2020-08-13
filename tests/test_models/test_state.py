#!/usr/bin/python3
""" Unittest for ``/models/state.py``
class State:
    class attributes:
        - __tablename__
        - name
        - cities
    0. __init__(self, *args, **kwargs) inherited from 'BaseModel'
    1. def cities(self) --- @property ---
python3 -m unittest tests/test_models/test_state.py
"""
import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """
    ------------------------------------------------------------
    Public class attributes
    ------------------------------------------------------------
    """
    def test_class_attributes(self):
        """ Tests for class attributes """
        self.assertTrue('__tablename__' in State.__dict__)
        self.assertTrue('name' in State.__dict__)
        self.assertTrue('cities' in State.__dict__)

    def test_type_attributes(self):
        """ check type """
        self.assertIsInstance(State.__tablename__, str)

    """
    ------------------------------------------------------------
    0. __init__(self, *args, **kwargs) inherited from 'BaseModel'
    ------------------------------------------------------------
    """
    def test_init_without_kwargs(self):
        """ test default init (attrs since BaseModel) """
        s = State()
        self.assertTrue('id' in s.__dict__)
        self.assertTrue('created_at' in s.__dict__)
        self.assertTrue('updated_at' in s.__dict__)
        self.assertIsInstance(s, BaseModel)

    def test_init_with_kwargs(self):
        """ test constructor: with **kwargs (attrs since BaseModel + attrs) """
        s = State(**{'__class__': "SomeClass",
                      'id': "f7f99",
                      'created_at': "2020-06-29T15:27:48.421135",
                      'updated_at': "2020-06-29T15:27:48.421148",
                      'name': "Antioquia"})
        """ must not create the key: __class__ """
        self.assertFalse('__class__' in s.__dict__)
        """ must create the keys """
        self.assertTrue('id' in s.__dict__)
        self.assertTrue('created_at' in s.__dict__)
        self.assertTrue('updated_at' in s.__dict__)
        self.assertTrue('name' in s.__dict__)

    """
    ------------------------------------------------------------
    1. def cities(self) --- @property ---
    ------------------------------------------------------------
    """
    def test_method_reviews(self):
        s = State()
        self.assertIsInstance(s.cities, list)
