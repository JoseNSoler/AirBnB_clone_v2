#!/usr/bin/python
""" Unittest for DB_Storage """
import pep8
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage
import MySQLdb
import unittest
import os

from os import getenv
from models.base_model import BaseModel
from models.user import User


@unittest.skipIf(
    os.getenv('HBNB_TYPE_STORAGE') != 'db',
    "This test only work in DBStorage")
class TestDBStorage(unittest.TestCase):
    """ testing """

    @classmethod
    def setUpClass(cls):
        """Tests"""
        cls.user = User()
        cls.user.first_name = "Mesa"
        cls.user.last_name = "diez"
        cls.user.email = "correo@hbtn.com"
        cls.storage = FileStorage()

    @classmethod
    def teardown(cls):
        """ testing """
        del cls.user

    def tearDown(self):
        """ testing """
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_DBStorage(self):
        """ testing """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(p.total_errors, 0, "pep8 errors")

    def test_new(self):
        """ testing """
        storage = FileStorage()
        obj = storage.all()
        user = User()
        user.name = "hbtn"
        storage.new(user)
        key = user.__class__.__name__ + "." + str(user.id)
        self.assertIsNotNone(obj[key])

    def test_all(self):
        """ testing """
        storage = FileStorage()
        obj = storage.all()
        self.assertIsNotNone(obj)
        self.assertEqual(type(obj), dict)
        self.assertIs(obj, storage._FileStorage__objects)

    def test_reload_dbtorage(self):
        """ testing """
        self.storage.save()
        Root = os.path.dirname(os.path.abspath("console.py"))
        path = os.path.join(Root, "file.json")
        with open(path, 'r') as f:
            lines = f.readlines()
        try:
            os.remove(path)
        except Exception:
            pass
        self.storage.save()
        with open(path, 'r') as f:
            lines2 = f.readlines()
        self.assertEqual(lines, lines2)
        try:
            os.remove(path)
        except Exception:
            pass
        with open(path, "w") as f:
            f.write("{}")
        with open(path, "r") as r:
            for line in r:
                self.assertEqual(line, "{}")
        self.assertIs(self.storage.reload(), None)


if __name__ == "__main__":
    unittest.main()