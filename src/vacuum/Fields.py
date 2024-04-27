from .Model import Field
from .Item import MainItem

@MainItem.register
class PublishDate(Field):
    xpaths:list[str]
    regex_list:list[str]
@MainItem.register
class Contact(Field):
    ...
@MainItem.register
class ProductTitle(Field):
    ...
@MainItem.register
class PublishLink(Field):
    ...
@MainItem.register
class ProductPrice(Field):
    ...
@MainItem.register
class VendorLocation(Field):
    ...