#!/usr/bin/python3
""" importing modules for the FileStorage testing """
import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """ testing the FileStorage class """
    def setUp(self):
        """ setting up resources """
        self.test_file = "test_file.json"
        with open(self.test_file, "w") as f:
            f.write('{"BaseModel.123": {"id": "123","created_at": "2023-08-10T12:00:00"}}')
        self.file_storage = FileStorage()
        self.file_storage._FileStorage__file_path = self.test_file

    def tearDown(self):
        """ cleaning up used resources """
        if os.path.exists(self.file_storage._FileStorage__file_path):
            os.remove(self.file_storage._FileStorage__file_path)

    def test_all_method_return(self):
        """ testing returns of methods """
        model1 = BaseModel()
        model2 = BaseModel()

        self.file_storage.new(model1)
        self.file_storage.new(model2)

        all_objects = self.file_storage.all()

        self.assertTrue(isinstance(all_objects, dict))

    def test_save_creates_file_and_not_empty(self):
        """ testing that json file exists """
        model1 = BaseModel()
        model2 = BaseModel()

        self.file_storage.new(model1)
        self.file_storage.new(model2)

        self.file_storage.save()

        self.assertTrue(os.path.exists(self.file_storage.
                                       _FileStorage__file_path))
        self.assertTrue(os.path.getsize(self.file_storage.
                                       _FileStorage__file_path) > 0)

    def test_reload_with_existing_file(self):

        # Create a new BaseModel and save it
        model1 = BaseModel()
        self.file_storage.new(model1)
        self.file_storage.save()

        # Reload the data
        self.file_storage.reload()

        # Check if the expected object is in __objects
        self.assertIn('BaseModel.' + model1.id, self.file_storage._FileStorage__objects)
        self.assertIsInstance(self.file_storage._FileStorage__objects['BaseModel.' + model1.id], BaseModel)

    def test_reload_with_non_existing_file(self):
        self.file_storage._FileStorage__file_path = "non_existing_file.json"

        try:
            self.file_storage.reload()
        except Exception as e:
            self.fail(f"reload method raised an unexpected exception: {e}")


if __name__ == "__main__":
    """ test entry point """
    unittest.main()
