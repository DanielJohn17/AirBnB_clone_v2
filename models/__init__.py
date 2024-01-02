#!/usr/bin/python3
"""__init__ magic method for models directory"""
from os import getenv
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage


storage_env = getenv("HBNB_TYPE_STORAGE")

if storage_env == "db":
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()
