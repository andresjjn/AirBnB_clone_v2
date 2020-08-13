#!/usr/bin/python3
""" Unittest for ``/models/review.py``
class Review:
    class attributes:
        - __tablename__
        - text
        - place_id
        - user_id
    0. __init__(self, *args, **kwargs) inherited from 'BaseModel'
python3 -m unittest tests/test_models/test_review.py
"""
import unittest
from models.base_model import BaseModel
from models.review import Review

class TestReview(unittest.TestCase):
    """
    ------------------------------------------------------------
    class attributes
    ------------------------------------------------------------
    """
    def test_attributes(self):
        """ Tests for class attributes """
        self.assertTrue('place_id' in Review.__dict__)
        self.assertTrue('user_id' in Review.__dict__)
        self.assertTrue('text' in Review.__dict__)

    def test_type_attributes(self):
        """ check type """
        self.assertIsInstance(Review.__tablename__, str)

    """
    ------------------------------------------------------------
    0. __init__(self, *args, **kwargs) inherited from 'BaseModel'
    ------------------------------------------------------------
    """
    def test_init_without_kwargs(self):
        """ test default init (attrs since BaseModel) """
        r = Review()
        self.assertTrue('id' in r.__dict__)
        self.assertTrue('created_at' in r.__dict__)
        self.assertTrue('updated_at' in r.__dict__)
        self.assertIsInstance(r, BaseModel)

    def test_init_with_kwargs(self):
        """ test constructor: with **kwargs (attrs since BaseModel + attrs) """
        r = Review(**{'__class__': "SomeClass",
                       'id': "f7f99",
                       'created_at': "2020-06-29T15:27:48.421135",
                       'updated_at': "2020-06-29T15:27:48.421148",
                       'name': "Diana Caro"})
        """ must not create the key: __class__ """
        self.assertFalse('__class__' in r.__dict__)
        """ must create the keys """
        self.assertTrue('id' in r.__dict__)
        self.assertTrue('created_at' in r.__dict__)
        self.assertTrue('updated_at' in r.__dict__)
        self.assertTrue('name' in r.__dict__)
