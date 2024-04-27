from .Model import Field
from .Item import MainItem
from itertools import product

@MainItem.register
class ProductTitle(Field):
    title = '{}[class=contains("title")][1]'.format
    header_tags = ['h2','h3','h4','h5',title('p'),title('div')]
    data = ['a[1]/@title','a[1]/text()','text()']
    xpaths = [*map('/'.join,product(header_tags,data))]
@MainItem.register
class PublishDate(Field):
    div = 'div[class=contains("{}")]'.format
    date_tags = [div('date'),div('time')]
    data = ['text()','span[1]/text()']
    xpaths = [*map('/'.join,product(date_tags,data))]+[
        'span/@data-bs-content',
        'div[ class="media-body"]/p[1]/text()'
    ]
@MainItem.register
class Contact(Field):
    types = [
        'tel',
        'sms',
        'whatsapp'
    ]
    xpaths = list(map('a/@href[starts_with("{}:")]'.format,types))
@MainItem.register
class PublishLink(Field):
    ...
@MainItem.register
class ProductPrice(Field):
    ...
@MainItem.register
class VendorLocation(Field):
    ...