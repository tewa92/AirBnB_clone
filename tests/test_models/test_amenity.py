#!/usr/bin/python3
"""This script contains the test class for Amenity."""

from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """Test class for Amenity."""

    def __init__(self, *args, **kwargs):
        """Initialize test class."""
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """Test Amenity name attribute."""
        new = self.value()
        self.assertEqual(type(new.name), str)
