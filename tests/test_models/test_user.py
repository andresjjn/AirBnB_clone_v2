#!/usr/bin/python3
""" Unittest for ``/models/user.py``
class User:
    class attributes:
        - __tablename__
        - email
        - password
        - first_name
        - last_name
        - places
        - reviews
    0. __init__(self, *args, **kwargs) inherited from 'BaseModel'
python3 -m unittest tests/test_models/test_user.py
"""
import unittest
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """
    ------------------------------------------------------------
    class attributes
    ------------------------------------------------------------
    """
    def test_class_attributes(self):
        """ tests for class attributes """
        self.assertTrue('__tablename__' in User.__dict__)
        self.assertTrue('email' in User.__dict__)
        self.assertTrue('password' in User.__dict__)
        self.assertTrue('first_name' in User.__dict__)
        self.assertTrue('last_name' in User.__dict__)
        self.assertTrue('places' in User.__dict__)
        self.assertTrue('reviews' in User.__dict__)

    def test_type_attributes(self):
        """ check type """
        self.assertIsInstance(User.__tablename__, str)

    """
    ------------------------------------------------------------
    0. __init__(self, *args, **kwargs) inherited from 'BaseModel'
    ------------------------------------------------------------
    """
    def test_init_without_kwargs(self):
        """ test default init (attrs since BaseModel) """
        u = User()
        self.assertTrue('id' in u.__dict__)
        self.assertTrue('created_at' in u.__dict__)
        self.assertTrue('updated_at' in u.__dict__)
        self.assertIsInstance(u, BaseModel)

    def test_init_with_kwargs(self):
        """ test constructor: with **kwargs (attrs since BaseModel + attrs) """
        u = User(**{'__class__': "SomeClass",
                     'id': "f7f99",
                     'created_at': "2020-06-29T15:27:48.421135",
                     'updated_at': "2020-06-29T15:27:48.421148",
                     'name': "Diana Caro"})
        """ must not create the key: __class__ """
        self.assertFalse('__class__' in u.__dict__)
        """ must create the keys """
        self.assertTrue('id' in u.__dict__)
        self.assertTrue('created_at' in u.__dict__)
        self.assertTrue('updated_at' in u.__dict__)
        self.assertTrue('name' in u.__dict__)
