#!/usr/bin/python3
"""Test User"""
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.user import User


class TestState(unittest.TestCase):
    """Test State file"""

    def tearDown(self):
        ''' After tests, remove json file '''
        try:
            remove("file.json")
        except Exception:
            pass

    def test_class(self):
        """Test the class."""
        user1 = User()
        self.assertTrue(hasattr(user1, "id"))
        self.assertTrue(hasattr(user1, "created_at"))
        self.assertTrue(hasattr(user1, "updated_at"))
        self.assertEqual(user1.__class__.__name__, "User")

    def test_father(self):
        """Test the class - BaseModel """
        user1 = User()
        self.assertTrue(issubclass(user1.__class__, BaseModel))

    def test_class_kwargs(self):
        """Test attributes."""
        user1 = User()
        self.assertTrue(hasattr(user1, "updated_at"))
        self.assertTrue(hasattr(user1, "created_at"))
        self.assertTrue(hasattr(user1, "id"))
        self.assertTrue(hasattr(user1, "email"))
        self.assertTrue(hasattr(user1, "password"))
        self.assertTrue(hasattr(user1, "first_name"))
        self.assertTrue(hasattr(user1, "last_name"))
        self.assertEqual(type(user1.updated_at), datetime)
        self.assertEqual(type(user1.created_at), datetime)
        self.assertEqual(type(user1.id), str)
        self.assertFalse(hasattr(user1, "Manga"))
        self.assertEqual(type(user1.email), str)
        self.assertEqual(type(user1.password), str)
        self.assertEqual(type(user1.first_name), str)
        self.assertEqual(type(user1.last_name), str)

    def test_father_kwargs(self):
        """Test the class - BaseModel passing kwargs """
        dictonary = {'id': '662a23b3-abc7-4f43-81dc-64c000000c00'}
        user1 = User(**dictonary)
        self.assertTrue(issubclass(user1.__class__, BaseModel))

    def test_State(self):
        """Test attributes of the class."""
        my_State = User()
        my_State.name = "LA"
        self.assertEqual(my_State.name, 'LA')

    def test_attribute(self):
        """Test assigned attributes."""
        user1 = User()
        user1.place_id = "13"
        user1.text = "text"
        self.assertEqual(type(user1.place_id), str)
        self.assertEqual(type(user1.text), str)
