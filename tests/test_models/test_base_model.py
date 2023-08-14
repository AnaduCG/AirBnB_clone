#!/usr/bin/python3
""" importing models for base model unittest """
import os
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime
from unittest.mock import patch


class TestBaseModel(unittest.TestCase):
    """ testing for the BadeModel class functionalities """
    def setUp(self):
        """ setting up needed resources """
        self.models = [BaseModel() for _ in range(10)]
        self.model = BaseModel()
    
    def test_str_representation(self):
        i = BaseModel()
        i.name = "My First Model"
        i.my_number = 89
        expected_output = f"[BaseModel] ({i.id}) {i.__dict__}"
        self.assertEqual(str(i), expected_output)
    
    def test_id_str(self):
        """ checking id data type is string """
        self.assertTrue(isinstance(self.model.id, str))

    def test_created_at_exists(self):
        """ checking if the created_at instance exists """
        self.assertTrue(hasattr(self.model, 'created_at'))

    def test_updated_at_exists(self):
        """ checking if the updated_at instance exists """
        self.assertTrue(hasattr(self.model, 'updated_at'))

    def test_id_exists(self):
        """ checking if the id_at instance exists """
        self.assertTrue(hasattr(self.model, 'id'))

    def test_id_unique(self):
        """ checking if id is unique """
        ids = [model.id for model in self.models]
        self.assertEqual(len(ids), len(set(ids)))

    def test_created_at_type(self):
        """ ensuring that created_at is a datetime """
        self.assertIsInstance(self.model.created_at, datetime)

    def test_updated_at_type(self):
        """ ensuring that created_at is a datetime """
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_to_dict_returns_dict(self):
        """ ensuring that the method to_dict returns a dictionary format """
        data = self.model.to_dict()
        self.assertIsInstance(data, dict)

    def test_to_dict_keys(self):
        """ testing to_dict returns required dictionary keys """
        expected_keys = ['id', 'created_at', 'updated_at', '__class__']
        data = self.model.to_dict()
        self.assertCountEqual(expected_keys, data.keys())

    def test_to_dict_values(self):
        """ testing to_dict returns required dictionary keys """
        data = self.model.to_dict()
        for key, value in data.items():
            if key == '__class__':
                self.assertEqual(value, self.model.__class__.__name__)
            else:
                self.assertEqual(getattr(self.model, key), value)

    def test_no_args_in_constructor(self):
        """ testing that BaseModel doesn't use *args """
        try:
            BaseModel()
        except TypeError:
            self.fail("*args are not to be used")

    def test_init_with_kwargs(self):
        """ testing the *kwargs usage """
        kwargs = {
            'id': 'test_id',
            'created_at': '2022-08-10T12:34:56.789012',
            'updated_at': '2022-08-11T12:34:56.789012',
            'my_attr': 'attr_value'
        }

        instance = BaseModel(**kwargs)

        self.assertEqual(instance.id, 'test_id')
        self.assertIsInstance(instance.created_at, datetime)
        self.assertEqual(instance.created_at.strftime('%Y-%m-%dT%H:%M:%S.%f'),
                         '2022-08-10T12:34:56.789012')
        self.assertIsInstance(instance.updated_at, datetime)
        self.assertEqual(instance.updated_at.strftime('%Y-%m-%dT%H:%M:%S.%f'),
                         '2022-08-11T12:34:56.789012')


class TestBaseModelFileStorageLink(unittest.TestCase):
    """testing for BaseModel and FileStorage linking

    Args:
        unittest (module): python unittest module
    """
    def setUp(self):
        """ setting up resources
        """
        self.test_file = "test_file.json"
        self.file_storage = FileStorage()
        self.file_storage._FileStorage__file_path = self.test_file

    def tearDown(self):
        """ clearing up used resources """
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    @patch('models.engine.file_storage.FileStorage.save')
    def test_base_model_saves_using_file_storage(self, mock_save):
        """ Create an instance of BaseModel """
        model = BaseModel()
        model.save()
        """ This should call the save method of FileStorage """
        model = BaseModel()

        """ Assert that the mock save method was called """
        mock_save.assert_called_once()

        """ Manually reload the data from the test file """
        self.file_storage.reload()

        """ Check if the BaseModel instance is in the storage """
        key = 'BaseModel.' + model.id
        self.assertIn(key, self.file_storage._FileStorage__objects)
        saved_model = self.file_storage._FileStorage__objects[key]

        """ Check if the saved_model is indeed an instance of BaseModel """
        self.assertIsInstance(saved_model, BaseModel)

    def test_new_method_called_on_init(self):
        """ Create an instance of BaseModel using __init__ """
        model = BaseModel()

        """ Manually reload the data from the test file """
        self.file_storage.reload()

        """ Check if the BaseModel instance is in the storage """
        key = 'BaseModel.' + model.id
        self.assertIn(key, self.file_storage._FileStorage__objects)
        saved_model = self.file_storage._FileStorage__objects[key]

        """ Check if the saved_model is indeed an instance of BaseModel """
        self.assertIsInstance(saved_model, BaseModel)

    def test_new_method_not_called_on_dict_init(self):
        """ Create an instance of BaseModel using dictionary representation """
        model_dict = {
            'id': '123',
            'created_at': '2023-08-10T12:00:00.123456'
        }
        model = BaseModel(**model_dict)

        """ Manually reload the data from the test file """
        self.file_storage.reload()

        """ Check if the BaseModel instance is not in the storage """
        key = 'BaseModel.' + model.id
        self.assertNotIn(key, self.file_storage._FileStorage__objects)


if __name__ == "__main__":
    """ entry point """
    unittest.main()
