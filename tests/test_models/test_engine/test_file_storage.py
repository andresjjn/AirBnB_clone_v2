#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
from models.base_model import BaseModel
from models import storage
import os
import json
import pep8
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class test_fileStorage(unittest.TestCase):
    """ Class to test the file storage method """

    def setUp(self):
        """ Set up test environment """
        del_list = []
        for key in storage._FileStorage__objects.keys():
            del_list.append(key)
        for key in del_list:
            del storage._FileStorage__objects[key]

    def tearDown(self):
        """ Remove storage file at end of tests """
        try:
            os.remove('file.json')
        except:
            pass

    def test_obj_list_empty(self):
        """ __objects is initially empty """
        self.assertEqual(len(storage.all()), 0)

    def test_new(self):
        """ New object is correctly added to __objects """
        new = BaseModel()
        for obj in storage.all().values():
            temp = obj
        self.assertTrue(temp is obj)

    def test_all(self):
        """ __objects is properly returned """
        new = BaseModel()
        temp = storage.all()
        self.assertIsInstance(temp, dict)

    def test_base_model_instantiation(self):
        """ File is not created on BaseModel save """
        new = BaseModel()
        self.assertFalse(os.path.exists('file.json'))

    def test_empty(self):
        """ Data is saved to file """
        new = BaseModel()
        thing = new.to_dict()
        new.save()
        new2 = BaseModel(**thing)
        self.assertNotEqual(os.path.getsize('file.json'), 0)

    def test_save(self):
        """ FileStorage save method """
        new = BaseModel()
        storage.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_reload(self):
        """ Storage file is successfully loaded to __objects """
        new = BaseModel()
        storage.save()
        storage.reload()
        for obj in storage.all().values():
            loaded = obj
        self.assertEqual(new.to_dict()['id'], loaded.to_dict()['id'])

    def test_reload_empty(self):
        """ Load from an empty file """
        with open('file.json', 'w') as f:
            pass
        with self.assertRaises(ValueError):
            storage.reload()

    def test_reload_from_nonexistent(self):
        """ Nothing happens if file does not exist """
        self.assertEqual(storage.reload(), None)

    def test_base_model_save(self):
        """ BaseModel save method calls storage save """
        new = BaseModel()
        new.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_type_path(self):
        """ Confirm __file_path is string """
        self.assertEqual(type(storage._FileStorage__file_path), str)

    def test_type_objects(self):
        """ Confirm __objects is a dict """
        self.assertEqual(type(storage.all()), dict)

    def test_key_format(self):
        """ Key is properly formatted """
        new = BaseModel()
        _id = new.to_dict()['id']
        for key in storage.all().keys():
            temp = key
        self.assertEqual(temp, 'BaseModel' + '.' + _id)

    def test_storage_var_created(self):
        """ FileStorage object storage created """
        from models.engine.file_storage import FileStorage
        print(type(storage))
        self.assertEqual(type(storage), FileStorage)


""" Unittest for ``/models/engine/file_storage.py``
class FileStorage:
    0. classes(self)
    1. all(self)
    2. new(self, obj)
    3. save(self)
    4. reload(self)
python3 -m unittest tests/test_models/test_engine/test_file_storage.py
"""


class TestFileStorage(unittest.TestCase):
    def classes(self):
        """ Method that return a dict of the classes """

        options = {'BaseModel': BaseModel,
                   'User': User,
                   'State': State,
                   'City': City,
                   'Amenity': Amenity,
                   'Place': Place,
                   'Review': Review}
        return options
    """ unittests """

    def setUp(self):
        """ resets __objects dictionary """
        FileStorage._FileStorage__objects = {}
        storage.save()

    """
    ------------------------------------------------------------
    0. classes(self)
    ------------------------------------------------------------
    """

    def test_classes(self):
        """ test if 'classes' returns a dict with the classes """
        dictionary = {'BaseModel': BaseModel,
                      'User': User,
                      'State': State,
                      'City': City,
                      'Amenity': Amenity,
                      'Place': Place,
                      'Review': Review}
        self.assertEqual(self.classes(), dictionary)

    """
    ------------------------------------------------------------
    1. all(self)
    ------------------------------------------------------------
    """

    def test_all(self):
        """ test if 'all' returns the content of __objects """
        FileStorage._FileStorage__objects = {'key': "object"}
        self.assertEqual(storage.all(), {'key': "object"})

    """
    ------------------------------------------------------------
    2. new(self, obj)
    ------------------------------------------------------------
    """

    def test_new(self):
        """ test if 'new' adds an object in __objects """
        u = User()
        storage.new(u)
        self.assertTrue(
            FileStorage._FileStorage__objects[type(u).__name__ + "." + u.id])

    """
    ------------------------------------------------------------
    3. save(self)
    ------------------------------------------------------------
    """

    def test_save(self):
        """ test if 'save' actually save the data in file.json """
        u = User()
        storage.new(u)
        storage.save()
        try:
            with open(FileStorage._FileStorage__file_path,
                      'r', encoding='utf-8') as file:
                objs_dict = json.load(file)
        except:
            raise ValueError
        key = type(u).__name__ + "." + u.id
        self.assertTrue(key in objs_dict)

    """
    ------------------------------------------------------------
    4. reload(self)
    ------------------------------------------------------------
    """

    def test_reload(self):
        """ test if 'reload' reads 'file.json' and fill __objects """
        u = User()
        storage.new(u)
        storage.save()
        FileStorage._FileStorage__objects = {}
        storage.reload()
        key = type(u).__name__ + "." + u.id
        self.assertTrue(key in FileStorage._FileStorage__objects)


class TestAmenity(unittest.TestCase):
    """Class test using unittest"""

    @classmethod
    def setUpClass(cls):
        """ set up the class """
        cls.prueba = User()
        cls.prueba.name = "team"
        cls.prueba.age = 25

    @classmethod
    def tearDown(cls):
        """ at the end it del the object """
        del cls.prueba

    def tearDown(self):
        """ at the end it remove the json """
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings).")

    def test_documentation(self):
        """ Verify the documentation """
        self.assertTrue(len(FileStorage.__doc__) > 1)
        self.assertTrue(len(FileStorage.all.__doc__) > 1)
        self.assertTrue(len(FileStorage.new.__doc__) > 1)
        self.assertTrue(len(FileStorage.save.__doc__) > 1)
        self.assertTrue(len(FileStorage.reload.__doc__) > 1)

    def test_args_kwargs(self):
        """ test args and kwargs input """
        self.assertEqual(self.prueba.name, "team")
        self.assertEqual(self.prueba.age, 25)
        self.assertTrue(hasattr(self.prueba, "name"))
        self.assertTrue(hasattr(self.prueba, "age"))
        self.assertEqual(self.prueba.__class__.__name__, "User")

    def test_all(self):
        """ test all in File Stroage """
        test = FileStorage()
        testall = test.all()
        self.assertIsNotNone(testall)
        self.assertEqual(type(testall), dict)

    def test_new(self):
        """ test new in File Stroage """
        test = FileStorage()
        testall = test.all()
        testnew = User()
        testnew.id = "666"
        testnew.name = "Anticristo"
        test.new(testnew)
        k = "{}.{}".format(testnew.__class__.__name__, testnew.id)
        self.assertIsNotNone(testall[k])

    def test_save(self):
        """ test save in File Stroage """
        test = FileStorage()
        obj = BaseModel()
        test.new(obj)
        testall = test.save()
        self.assertTrue(os.path.exists("file.json"))
