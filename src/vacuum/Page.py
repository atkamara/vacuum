from .Model import Page
from .Item import MainItem

class MainPage(Page):
    def as_item(self,html)->Item:
        return MainItem(html)