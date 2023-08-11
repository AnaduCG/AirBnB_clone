#!/usr/bin/python3
import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.file_storage = FileStorage()

    def tearDown(self):
        if os.path.exists(self.file_storage._FileStorage__file_path):
            os.remove(self.file_storage._FileStorage__file_path)

    def test_all_method_return(self):
            # Create instances of BaseModel and add them to the FileStorage
            model1 = BaseModel()
            model2 = BaseModel()

            # Add models to the FileStorage
            self.file_storage.new(model1)
            self.file_storage.new(model2)

            # Get all objects using the all method
            all_objects = self.file_storage.all()

            # Check if all_objects is a dictionary
            self.assertTrue(isinstance(all_objects, dict))

            # Check if the returned dictionary matches __objects
            self.assertEqual(all_objects, self.file_storage._FileStorage__object)

    @unittest.skip("Skip for now")
    def test_save_creates_file_and_not_empty(self):
            # Create instances of BaseModel and add them to the FileStorage
            model1 = BaseModel()
            model2 = BaseModel()

            # Add models to the FileStorage
            self.file_storage.new(model1)
            self.file_storage.new(model2)

            # Save the data to "file.json"
            self.file_storage.save()

            # Check if "file.json" exists and is not empty
            self.assertTrue(os.path.exists(self.file_storage._FileStorage__file_path))
            self.assertTrue(os.path.getsize(self.file_storage._FileStorage__file_path) > 0)

if __name__ == "__main__":
    unittest.main()
