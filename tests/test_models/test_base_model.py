#!/usr/bin/python3
'''
Test: BaseModel And pep8
'''

import io
import unittest
import unittest.mock
import pep8
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.state import State
from models.review import Review
from console import HBNBCommand
import test
from datetime import datetime


class Testpep8(unittest.TestCase):
    """Test pep8 with all files"""

    def test_pep8_amenity(self):
        """Test the pep8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_base_model(self):
        """Test the pep8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_city(self):
        """Test the pep8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_place(self):
        """Test the pep8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/place.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_review(self):
        """Test the pep8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_state(self):
        """Test the pep8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_user(self):
        """Test the pep8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_init(self):
        """Test the pep8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/__init__.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_file_storage(self):
        """Test the pep8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_console(self):
        """Test the pep8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_test_base_model(self):
        """Test the pep8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(
            ['tests/test_models/test_base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_test_amenity(self):
        """Test the pep8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(
            ['tests/test_models/test_amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_test_city(self):
        """Test the pep8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(
            ['tests/test_models/test_city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_test_state(self):
        """Test the pep8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(
            ['tests/test_models/test_state.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_test_place(self):
        """Test the pep8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(
            ['tests/test_models/test_place.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_test_review(self):
        """Test the pep8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(
            ['tests/test_models/test_review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_test_user(self):
        """Test the pep8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(
            ['tests/test_models/test_user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_test_console(self):
        """Test the pep8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(
            ['tests/test_console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


class test_base_model(unittest.TestCase):
    ''' Test class for base_model '''

    def tearDown(self):
        ''' After tests, remove json file '''
        try:
            remove("file.json")
        except Exception:
            pass

    def test_empty_constructor(self):
        ''' Create object without args/kwargs '''
        obj = BaseModel()
        self.assertTrue(hasattr(obj, 'id'))
        self.assertTrue(type(obj.id), str)
        self.assertTrue(hasattr(obj, 'created_at'))
        self.assertTrue(type(obj.created_at), datetime)
        self.assertTrue(hasattr(obj, 'updated_at'))
        self.assertTrue(type(obj.updated_at), datetime)

    def test_kwargs_constructor(self):
        ''' Create object passing Kwargs '''
        dictonary = {'id': 'cc9909cf-a909-9b90-9999-999fd99ca9a9',
                     'created_at': '2025-06-28T14:00:00.000001',
                     '__class__': 'BaseModel',
                     'updated_at': '2030-06-28T14:00:00.000001',
                     'score': 100
                     }

        obj = BaseModel(**dictonary)
        self.assertTrue(hasattr(obj, "__class__"))
        self.assertFalse(obj.__class__ == 'BaseModel')

        self.assertTrue(hasattr(obj, 'id'))
        self.assertTrue(hasattr(obj, 'created_at'))
        self.assertTrue(hasattr(obj, 'updated_at'))
        self.assertTrue(hasattr(obj, 'score'))

        self.assertTrue(type(obj.created_at), datetime)
        self.assertTrue(type(obj.updated_at), datetime)

        self.assertEqual(obj.id, 'cc9909cf-a909-9b90-9999-999fd99ca9a9')
        self.assertEqual(
            obj.created_at.isoformat(),
            '2025-06-28T14:00:00.000001')
        self.assertEqual(
            obj.updated_at.isoformat(),
            '2030-06-28T14:00:00.000001')
        self.assertEqual(obj.score, 100)

    def test_kwargs_constructor_2(self):
        ''' Create object passing Kwargs, without id and dates '''
        dictonary = {'score': 100}

        obj = BaseModel(**dictonary)
        self.assertTrue(hasattr(obj, 'id'))
        self.assertTrue(hasattr(obj, 'created_at'))
        self.assertTrue(hasattr(obj, 'updated_at'))
        self.assertTrue(hasattr(obj, 'score'))

    def test_empty_constructor_ids(self):
        ''' Test id generator '''
        obj = BaseModel()
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertTrue(obj.id != obj1.id)
        self.assertTrue(obj.id != obj2.id)
        self.assertTrue(obj1.id != obj2.id)

    def test_attr_nan(self):
        """NaN attribute."""
        obj = BaseModel(float("nan"))
        self.assertTrue(hasattr(obj, "id"))
        self.assertTrue(hasattr(obj, "created_at"))
        self.assertTrue(hasattr(obj, "updated_at"))

    def test_attr_inf(self):
        """Inf attribute."""
        obj = BaseModel(float("inf"))
        self.assertTrue(hasattr(obj, "id"))
        self.assertTrue(hasattr(obj, "created_at"))
        self.assertTrue(hasattr(obj, "updated_at"))

    def test_attr_none(self):
        """None attribute."""
        obj = BaseModel(None)
        self.assertTrue(hasattr(obj, "id"))
        self.assertTrue(hasattr(obj, "created_at"))
        self.assertTrue(hasattr(obj, "updated_at"))

    def test_str_method(self):
        ''' Test str method '''
        dictonary = {'id': 'cc9909cf-a909-9b90-9999-999fd99ca9a9',
                     'created_at': '2025-06-28T14:00:00.000001',
                     '__class__': 'BaseModel',
                     'updated_at': '2030-06-28T14:00:00.000001',
                     'score': 100
                     }

        obj = BaseModel(**dictonary)
        out = "[{}] ({}) {}\n".format(type(obj).__name__, obj.id, obj.__dict__)

        @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
        def assert_stdout(self, expected_output, mock_stdout):
            print(obj)
            self.assertEqual(mock_stdout.getvalue(), expected_output)

        def test_str(self):
            self.assert_stdout(out)

    def test_save_method(self):
        ''' Test save method '''
        obj = BaseModel()
        created = obj.created_at
        updated = obj.updated_at
        obj.save()
        self.assertTrue(created == obj.created_at)
        self.assertTrue(updated != obj.updated_at)

    def test_to_dict_method(self):
        ''' Test to_dict method '''
        obj = BaseModel(score=100)
        new_dict = obj.to_dict()

        self.assertEqual(new_dict['id'], obj.id)
        self.assertEqual(new_dict['score'], 100)
        self.assertEqual(new_dict['__class__'], 'BaseModel')
        self.assertEqual(new_dict['created_at'], obj.created_at.isoformat())
        self.assertEqual(new_dict['updated_at'], obj.updated_at.isoformat())

        self.assertEqual(type(new_dict['created_at']), str)
        self.assertEqual(type(new_dict['created_at']), str)

    def test_docstrings(self):
        """Tests for dosctrings"""
        self.assertGreater(len(BaseModel.__doc__), 1)
        self.assertGreater(len(BaseModel.__doc__), 1)
        self.assertGreater(len(BaseModel.__init__.__doc__), 1)
        self.assertGreater(len(BaseModel.__str__.__doc__), 1)
        self.assertGreater(len(BaseModel.save.__doc__), 1)
        self.assertGreater(len(BaseModel.to_dict.__doc__), 1)
