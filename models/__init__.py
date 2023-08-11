"""init_file creates a package"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()