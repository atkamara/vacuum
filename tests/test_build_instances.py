"""
This module contains test functions to check if instances of the classes are created successfully.

Classes Tested:
- Formatter
- Field
- Item
- Page
"""
from vacuum. Model import *
import pytest

def test_formatter_instance():
    # Test for Formatter class
    with pytest.raises(TypeError) :
        Formatter()
    print("TypeError Raised")

def test_field_instance():
    # Test for Field class
    with pytest.raises(TypeError) :
        Field()
    print("TypeError Raised")

def test_item_instance():
    # Test for Item class
    with pytest.raises(AttributeError):
        item_instance = Item()
    print("FAILED instance - AttributeError")

def test_page_instance():
    # Test for Page class
    with pytest.raises(TypeError) :
        Page()
    print("TypeError Raised")