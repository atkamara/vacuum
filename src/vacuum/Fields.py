from .Model import Field


class PublishDate(Field):
    xpaths:list[str]
    regex_list:list[str]
class Contact(Field):
    ...

class ProductTitle(Field):
    ...

class PublishLink(Field):
    ...

class ProductPrice(Field):
    ...

class VendorLocation(Field):
    ...