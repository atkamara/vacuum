from .Model import Field
from .Item import MainItem
from itertools import product
import re
from typing import Union
import dateparser

def ravel(value:Union[str,list[str],set(str)])->str:
    """
    This function takes a value as input, which can be a string, list of strings, or a set of strings.
    If the input is a set or list, the function concatenates the strings into a single string separated by spaces.
    Then, it removes newline characters and multiple spaces from the string.
    
    Parameters:
    value (Union[str,list[str],set(str)]): The input value to be raveled.
    
    Returns:
    str: The raveled string with removed newline characters and multiple spaces.
    """
    if isinstance(value,(set,list)):
        value = ' '.join(value)
    raveled = value.replace('\n',' ')
    removed_multiple_spaces = re.sub(r'\s+',' ',raveled)
    return removed_multiple_spaces
@MainItem.register
class ProductTitle(Field):
    title = '{}[class=contains("title")][1]'.format
    header_tags = ['h2','h3','h4','h5',title('p'),title('div')]
    data = ['a[1]/@title','a[1]/text()','text()']
    set_xpaths = lambda data : [*map('/'.join,product(header_tags,data))]
    xpaths = set_xpaths(data)
    def fmethod(self,value:str)->str:
        return ravel(value)
@MainItem.register
class PublishDate(Field):
    div = 'div[class=contains("{}")]'.format
    date_tags = [div('date'),div('time')]
    data = ['text()','span[1]/text()']
    xpaths = [*map('/'.join,product(date_tags,data))]+[
        'span/@data-bs-content',
        'div[ class="media-body"]/p[1]/text()']
@MainItem.register
class Contact(Field):
    types = [
        'tel',
        'sms',
        'whatsapp']
    xpaths = list(map('a/@href[starts_with("{}:")]'.format,types))
@MainItem.register
class PublishLink(Field):
    xpaths = ProductTitle.set_xpaths('a[1]/@href')
@MainItem.register
class ProductPrice(Field):
    price_test = '[class=contains("price")]'
    price_classes = f"*{price_test}"+"{}".format
    xpaths =[
        price_classes('//text()'),
        price_classes('/text()'),
        f'a{price_test}/@name',
        'h4[class="media-heading"]/span/text()']
@MainItem.register
class VendorLocation(Field):
    loc_tests = ['[class=contains("map")]','[contains("location")]']
    icon_tags = ['i','svg']
    icon_text = ['/text']
    parent = ['/..']
    data = ['/descendant[2]/text()','/text()']
    xpaths = list(map(''.join,product(icon_tags,loc_tests,parent,data)))+\
             list(map(''.join,product(icon_tags,icon_text,loc_tests,parent,data)))+[
            'img[src=contains(location)]/../text()'
    ]   