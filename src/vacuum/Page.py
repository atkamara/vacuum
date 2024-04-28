from .Model import Page
from .Item import MainItem

class MainPage(Page):
    xpath0 = "article"
    div = "div[@class={}]".format
    keywords = ["list(ing)?","item"]
    case0 = "[\s\-]".join(keywords) 
    case1 = "[\s\-]".join(reversed(keywords))
    cases = [case0,case1]
    regex = "|".join(cases)
    xpath1 = div(f'matches("{regex}")')
    xpath2 = div("media panel panel-default")
    xpaths = [xpath0,xpath1,xpath2]
    next_xpaths = [
        'a[id="prevnext"]',
        'li[class="pagi-next"]/a[1],'
        'a[class="page-link" and rel="next"]'
    ]
    def as_item(self,html):
        return MainItem(html)