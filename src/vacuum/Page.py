from .Model import Page
from .Item import MainItem

class MainPage(Page):
    xpath0 = '//article[contains(@class,"item")]'
    div = "//div[{}]".format
    xpath1 = div(f'contains(@class,"list") and contains(@class,"item")')
    xpath2 = div('@class="media panel panel-default"')
    xpaths = [xpath0,xpath1,xpath2]
    next_xpaths = [
        '//a[class="prevnext"]',
        '//a[class="page-link" and rel="next"]',
        '//li[class="pagi-next"]/a[1]',
        '//li.pagination-indicator/a/span[class="next"]/..' ]
    def as_item(self,html):
        return MainItem.relative_parse(html)