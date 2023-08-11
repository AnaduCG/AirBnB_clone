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
        model1 = BaseModel()
        model2 = BaseModel()

        self.file_storage.new(model1)
        self.file_storage.new(model2)

        all_objects = self.file_storage.all()

        self.assertTrue(isinstance(all_objects, dict))

        self.assertEqual(all_objects,
                         self.file_storage._FileStorage__object)

    @unittest.skip("Skip for now")
    def test_save_creates_file_and_not_empty(self):
        model1 = BaseModel()
        model2 = BaseModel()

        self.file_storage.new(model1)
        self.file_storage.new(model2)

        self.file_storage.save()

        self.assertTrue(os.path.exists(self.file_storage.
                                       _FileStorage__file_path))
        self.assertTrue(os.path.getsize(self.file_storage.
                                        _FileStorage__file_path) > 0)


if __name__ == "__main__":
    unittest.main()
