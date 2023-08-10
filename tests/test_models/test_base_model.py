#!/usr/bin/python3
""" importing models for base model unittest """
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """ testing for the BadeModel class functionalities """
    def setUp(self):
        """ setting up needed resources """
        self.models = [BaseModel() for _ in range(10)]
        self.model = BaseModel()

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


if __name__ == "__main__":
    unittest.main()
