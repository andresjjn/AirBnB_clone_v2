#!/usr/bin/python3
""" Unittest for ``/models/place.py``
class Place:
    class attributes:
        - __tablename__
        - city_id
        - user_id
        - name
        - description
        - number_rooms
        - number_bathrooms
        - max_guest
        - price_by_night
        - latitude
        - longitude
        - amenity_ids
        - reviews
    0. __init__(self, *args, **kwargs) inherited from 'BaseModel'
    1. def reviews(self) --- @property ---
python3 -m unittest tests/test_models/test_place.py
"""
import unittest
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """
    ------------------------------------------------------------
    class attributes
    ------------------------------------------------------------
    """
    def test_attributes(self):
        """ Tests for class attributes """
        self.assertTrue('__tablename__' in Place.__dict__)
        self.assertTrue('city_id' in Place.__dict__)
        self.assertTrue('user_id' in Place.__dict__)
        self.assertTrue('name' in Place.__dict__)
        self.assertTrue('description' in Place.__dict__)
        self.assertTrue('number_rooms' in Place.__dict__)
        self.assertTrue('number_bathrooms' in Place.__dict__)
        self.assertTrue('max_guest' in Place.__dict__)
        self.assertTrue('price_by_night' in Place.__dict__)
        self.assertTrue('latitude' in Place.__dict__)
        self.assertTrue('longitude' in Place.__dict__)
        self.assertTrue('amenity_ids' in Place.__dict__)
        self.assertTrue('reviews' in Place.__dict__)

    def test_type_attributes(self):
        """ check type """
        self.assertIsInstance(Place.__tablename__, str)

    """
    ------------------------------------------------------------
    0. __init__(self, *args, **kwargs) inherited from 'BaseModel'
    ------------------------------------------------------------
    """
    def test_init_without_kwargs(self):
        """ test default init (attrs since BaseModel) """
        p = Place()
        self.assertTrue('id' in p.__dict__)
        self.assertTrue('created_at' in p.__dict__)
        self.assertTrue('updated_at' in p.__dict__)
        self.assertIsInstance(p, BaseModel)

    def test_init_with_kwargs(self):
        """ test constructor: with **kwargs (attrs since BaseModel + attrs) """
        p = Place(**{'__class__': "SomeClass",
                     'id': "aaaaaaaa",
                     'created_at': "2020-06-29T15:27:48.421135",
                     'updated_at': "2020-06-29T15:27:48.421148",
                     'name': "a_place"})
        """ must not create the key: __class__ """
        self.assertFalse('__class__' in p.__dict__)
        """ must create the keys """
        self.assertTrue('id' in p.__dict__)
        self.assertTrue('created_at' in p.__dict__)
        self.assertTrue('updated_at' in p.__dict__)
        self.assertTrue('name' in p.__dict__)

    """
    ------------------------------------------------------------
    1. def reviews(self) --- @property ---
    ------------------------------------------------------------
    """
    def test_method_reviews(self):
        p = Place()
        self.assertIsInstance(p.reviews, list)
