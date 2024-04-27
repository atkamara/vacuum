"""
This module contains test functions to check if instances of the classes are created successfully.

Classes Tested:
- Formatter
- Field
- Item
- Page
"""
from vacuum import Model

def test_formatter_instance():
    # Test for Formatter class
    formatter_instance = Formatter()
    assert isinstance(formatter_instance, Formatter)
    print("Formatter instance is of the expected class type.")

def test_field_instance():
    # Test for Field class
    field_instance = Field()
    assert isinstance(field_instance, Field)
    print("Field instance is of the expected class type.")

def test_item_instance():
    # Test for Item class
    item_instance = Item()
    assert isinstance(item_instance, Item)
    print("Item instance is of the expected class type.")

def test_page_instance():
    # Test for Page class
    page_instance = Page()
    assert isinstance(page_instance, Page)
    print("Page instance is of the expected class type.")