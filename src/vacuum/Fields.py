from .Model import Field
from .Item import MainItem
from itertools import product

@MainItem.register
class ProductTitle(Field):
    title = '{}[class=contains("title")][1]'.format
    header_tags = ['h2','h3','h4','h5',title('p'),title('div')]
    child = ['a[1]','']
    data = ['@title','::text()']
    xpaths = ['/'.join(p for p in case if p) for case in product(header_tags,child,data)]
@MainItem.register
class PublishDate(Field):
    xpaths = [
        'div[class="listing-card__header__date"]/text()',
        'span/@data-bs-content',
        'div[class="card-title ad__card-timesince"]/span/text()'
    ]
@MainItem.register
class Contact(Field):
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