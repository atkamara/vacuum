from .Model import Field
from itertools import product
from functools import lru_cache
import re
from typing import Union
import dateparser
from .Item import MainItem

root=['//']
phone=r'[\s\-]{0,1}?'.join([
                r'\+{0,1}?\d{0,3}',
                r'(\d{2}',
                r'\d{3}',
                r'\d{2}',
                r'\d{2})'
                ])
currency = r'(\d{1}.*?)[^\d\s,.]'

@lru_cache(maxsize=None)
def get_relative(paths:tuple):
    return [
        re.sub(r'^\/+','descendant::',path)
        for path in paths
    ]
def ravel(value:Union[str,list[str],set[str]],sep=' ')->str:
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
        value = sep.join(set(value))
    raveled = value.replace('\n',' ')
    removed_multiple_spaces = re.sub(r'\s+',' ',raveled)
    return removed_multiple_spaces.strip()
@MainItem.register
class ProductTitle(Field):
    title = '{}[contains(@class,"title")][1]'.format
    header_tags = ['h2','h3','h4','h5',title('p'),title('div')]
    data = ['a[1]/@title','a[1]/text()','text()']
    xpaths = [*map('/'.join,product(root,header_tags,data))]
    relative_xpaths = get_relative(tuple(xpaths))
    def fmethod(self,value:str)->str:
        return ravel(value)
@MainItem.register
class PublishDate(Field):
    div = 'div[contains(@class,"{}")]'.format
    date_tags = [div('date'),div('time')]
    data = ['text()','span[1]/text()']
    xpaths = [*map('/'.join,product(root,date_tags,data))]+[
        'span/@data-bs-content',
        'div[ class="media-body"]/p[1]/text()']
    relative_xpaths = get_relative(tuple(xpaths))
    def fmethod(self,value:str)->str:
        return dateparser.parse(ravel(value)).isoformat()
@MainItem.register
class Contact(Field):
    types = [
        'tel',
        'sms',
        'whatsapp']
    xpaths = list(map(r'//a[starts-with(@href,"{}:")]/@href'.format,types))
    relative_xpaths = get_relative(tuple(xpaths))
    def fmethod(self,value:str)->str:
        return re.sub('[\s\-\+]','',';'.join(set(re.findall(phone,ravel(value)))))
@MainItem.register
class PublishLink(Field):
    title = '{}[contains(@class,"title")][1]'.format
    header_tags = ['h2','h3','h4','h5',title('p'),title('div')]
    xpaths =[*map('/'.join,product(root,header_tags,['a[1]/@href']))]+['//a[contains(@class,listing)][1]/@href']
    relative_xpaths = get_relative(tuple(xpaths))
    def fmethod(self,value:str)->str:
        return ravel(value,sep=';')
@MainItem.register
class ProductPrice(Field):
    price_test1 = '[contains(@class,"price")]'
    price_test2 = '[contains(name(),"price")]'
    price_classes = (f"//*{price_test1}"+"{}").format
    xpaths =[
        price_classes('//text()'),
        price_classes('/text()'),
        f'//a/@*{price_test2}',
        '//h4[class="media-heading"]/span/text()']
    relative_xpaths = get_relative(tuple(xpaths))
    def fmethod(self,value:str)->str:
        return re.sub('[\s,\.]','',';'.join(re.findall(currency,ravel(value,sep=';'))))
@MainItem.register
class VendorLocation(Field):
    loc_tests = ['[contains(@class,"map")]','[contains(@class,"location")]']
    icon_tags = ['i','svg']
    icon_text = ['/text']
    parent = ['/..']
    data = ['/descendant[2]/text()','/text()']
    xpaths = list(map(''.join,product(root,icon_tags,loc_tests,parent,data)))+\
             list(map(''.join,product(root,icon_tags,icon_text,loc_tests,parent,data)))+[
            '//img[contains(@src,"location")]/../text()']
    relative_xpaths = get_relative(tuple(xpaths))
    def fmethod(self,value:str)->str:
        return ravel(value)   