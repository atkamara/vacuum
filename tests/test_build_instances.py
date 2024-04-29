"""
This module contains test functions to check if instances of the classes are created successfully.

Classes Tested:
- Formatter
- Field
- Item
- Page
"""
from vacuum import Model
from vacuum import Item
from scrapy import Selector
from dataclasses import dataclass

import pytest

def test_formatter_instance():
    # Test for Formatter class
    with pytest.raises(TypeError) :
        Model.Formatter()
    print("TypeError Raised")

def test_field_instance():
    # Test for Field class
    with pytest.raises(TypeError) :
        Model.Field()
    print("TypeError Raised")

def test_item_instance():
    # Test for Item class
    item = Model.Item()
    isinstance(item,Model.Item)

def test_page_instance():
    # Test for Page class
    with pytest.raises(TypeError) :
        Model.Page()
    print("TypeError Raised")

def test_MainItem_instance():
    # Test for Page class
    html = '''<div></div>'''
    mi = Item.MainItem.parse(Selector(text=html))
    assert mi.__class__.__name__ == 'MainItem'