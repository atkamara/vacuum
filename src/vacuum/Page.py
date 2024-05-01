from .Model import Page
from .Item import MainItem
from .dbModel import MainItem as MainTable

class MainPage(Page):
    xpath0 = '//article[contains(@class,"item") and not(contains(@class,"cart"))]'
    div = "//div[{}]".format
    xpath1 = div(f'contains(@class,"list") and contains(@class,"item") ')
    xpath2 = div('@class="media panel panel-default"')
    xpaths = [xpath0,xpath1,xpath2]
    next_test = 'contains(@class,"next") or contains(@rel,"next")'
    next_xpaths = [
        f'//a[{next_test}]/@href',
        '//*[contains(@class,"next")]/a[1]/@href'
        ]
    sql_table = MainTable
    def as_item(self,html):
        return MainItem.parse(html,method='relative_value')